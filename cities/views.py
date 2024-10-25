from django.shortcuts import render
from .models import City
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Cityserializer
from django.http import Http404
# from drf_api.permissions import IsOwnerOrReadOnly

from rest_framework import generics
from .models import City, NewCity
from .serializers import Cityserializer, NewCitySerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication



# class CityListCreateView(generics.ListCreateAPIView):
#     queryset=City.objects.all()
#     serializer_class=Cityserializer
#     permission_classes=[IsAuthenticated]
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=City.objects.all()
#     serializer_class=Cityserializer
#     permission_classes= [IsAuthenticated]

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


