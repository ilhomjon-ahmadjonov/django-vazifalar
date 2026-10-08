from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework.response import Response
from .models import CustomUser,Verify,NEW,CODE_VERIFY, VIA_EMAIL,VIA_PHONE
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from datetime import datetime
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = CustomUser.objects.all()

class VerifyCodeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        code = request.data.get('code')
        user = request.user

        current_code = Verify.objects.all().filter(user=user,code=code, used=False, expire_time__gte=datetime.now()).first()

        if current_code is None:
            raise ValidationError('Kod xato yoki eskirgan')
        
        if user.auth_status == NEW:
                current_code.used = True
                current_code.save()

                user.auth_status = CODE_VERIFY
                user.save()

        return Response({
            'auth_status': user.auth_status,
            'msg': "code_verify" 
        })

class GetNewCodeView(APIView):
     def get(self,request):
        user = request.user

        codes = user.codes.all().filter(used=False, expire_time__gte=datetime.now()).exists()


          
        if codes:
            raise ValidationError('Sizda hali active kod bor')
        
        if user.auth_status == NEW:
            if user.auth_type == VIA_EMAIL:
                code = user.generate_code(user.auth_type)
                print(f'CODE EMAIL: {code} =========================')

                # send_mail(user.email,code)
            elif user.auth_type == VIA_PHONE:
                code = user.generate_code(user.auth_type)
                print(f'CODE PHONE: {code} =========================')
                 # send_mail(user.email,code)

        return Response({
            'msg': 'Code yuborildi',
            'auth_type': user.auth_type
        })

class TokenRefresh(APIView):
    permission_classes = [permissions.AllowAny]
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