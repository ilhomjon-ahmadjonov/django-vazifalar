from django.shortcuts import render
from .models import Account
from .serializer import SignUpSerializer,LoginSerializer,ProfileSerializer,ProfileUpdateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class SignUpView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
    queryset = Account.objects.all()

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

class ProfileView(APIView):
    def get(self,request):
        user = request.user
        serializer = ProfileSerializer(user)

        return Response(serializer.data)
class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer

    def get_object(self):
        return self.request.user

class TokenRefresh(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        refresh = request.data.get('refresh')
        try:
            refresh_token = RefreshToken(refresh)
        except:
            raise ValidationError('Token invalid')
        else:
            return Response({
                'access':str(refresh_token.access_token)
            })

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            if not refresh_token:
                return Response(
                    {"error": "Refresh token kiritilishi shart"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Tizimdan muvaffaqiyatli chiqdingiz (Logout)"},
                status=status.HTTP_205_RESET_CONTENT
            )
        except Exception:
            return Response(
                {"error": "Token yaroqsiz yoki allaqachon muddati o'tgan"},
                status=status.HTTP_400_BAD_REQUEST
            )