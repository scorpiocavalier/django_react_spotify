from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
class RoomView(generics.ListAPIView):
  # queryset is what fields we want returned
  queryset = Room.objects.all()
  # transform it to a more readable format
  serializer_class = RoomSerializer