from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.exceptions import NotFound
from .models import Hotel
from rest_framework.generics import  get_object_or_404
from .serializers import  HotelSerializers
# Create your views here.

class HotelListCreateView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

    
class HotelCreateView(generics.CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class HotelUpdateView(generics.UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class HotelDeleteView(generics.DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class HotelDetailView(generics.RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class =  HotelSerializers
    