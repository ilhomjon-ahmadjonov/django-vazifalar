from django.shortcuts import render
from .models import Customuser
from .serializer import SignUpSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class SignUpView(APIView):
    def post(self,request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data.pop('conf_pass')
        user = Customuser.objects.create_user(**serializer.validated_data)

        return Response({
            'msg': "Ro'yxatdan o'tdingiz",
            'data': SignUpSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "msg": 'Login',
            "token": token.key
        },status=status.HTTP_200_OK)

class LogOutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        Token.objects.filter(username=request.user).delete()

        return Response({
            'msg': 'Tizimdan chiqdingiz'
        }, status=status.HTTP_200_OK) 
