from django.shortcuts import render
from .models import Pix
from rest_framework import generics
from .serializers import CabezasSerializer


class PixCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Pix.objects.all(),
    serializer_class = CabezasSerializer


class PixList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Pix.objects.all(),
    serializer_class = CabezasSerializer

# Create your views here.
