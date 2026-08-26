from django.shortcuts import render
from .models import CustomUser
from .serializer import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def signup_view(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = CustomUser(**serializer.validated_data)
    user.set_password(serializer.validated_data['password'])
    user.save()

    serializer = SignUpSerializer(user)


    return Response({
        'msg': "signup",
        'data': serializer.data
    },status=status.HTTP_201_CREATED)