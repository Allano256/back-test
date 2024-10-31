from django.shortcuts import render

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import  NewCity
from .serializers import  NewCitySerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication



class NewCityView(generics.ListCreateAPIView):
    queryset=NewCity.objects.all()
    serializer_class=NewCitySerializer
    permissions_class=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Return only items owned by the current user
        return NewCity.objects.filter(user=self.request.user)


class NewCityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=NewCity.objects.all()
    serializer_class= NewCitySerializer
    permission_classes=[IsAuthenticated]


