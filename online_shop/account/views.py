from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework.response import Response
from .models import CustomUser,Verify
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
# Create your views here.
class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = CustomUser.objects.all()
    