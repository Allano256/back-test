from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def root_route(request):
    """
    This view will give a message on the landing page of the API.
    """

    return Response({"message": "Welcome to the Remember API..."})
