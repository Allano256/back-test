from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import SignUpSerializer, LoginSerializer
from .tokens import create_jwt_pair_for_user
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import logging

logger = logging.getLogger(__name__)


class SignUpView(generics.GenericAPIView):
    """
    This view handles the signup of user.
    """

    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        data = request.data

        serializer = SignUpSerializer(data=data)

        if serializer.is_valid():
            password_hash = make_password(
                serializer.validated_data.get("password")
                )

            user = User.objects.create(
                email=serializer.validated_data.get("email"),
                first_name=serializer.validated_data.get("first_name"),
                last_name=serializer.validated_data.get("last_name"),
                password=password_hash,
                is_active=True,
            )

            user.save()

            response = {
                "message": "User Created Successfully", "data": serializer.data
                }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    """
    This view handles the login of user.
    """

    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.get(email=email)

        if user and check_password(password, user.password):

            tokens = create_jwt_pair_for_user(user)

            # response = {"message": "Login Successfull", "tokens": tokens}
            response = {
                    "message": "Login Successful",
                    "tokens": tokens,
                    "user": {
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "username": user.username,
                    }
                }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            logger.info("User {}".format(user))
            return Response(data={
                "message": "Invalid email or password"}, status=400)
