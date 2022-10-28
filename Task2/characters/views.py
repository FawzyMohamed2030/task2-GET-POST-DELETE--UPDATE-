from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics , permissions
from . import models
from .serializers import Caractersserializer
class getcharacters(generics.CreateAPIView):
    serializer_class = Caractersserializer
    permission_classes = [permissions.IsAuthenticated]

class postcharacters(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Caractersserializer
    queryset = models.Characters.objects.all()

