from rest_framework import serializers,status
from .models import CustomUser
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.db.models import Q

class SignUpSerializer(serializers.ModelSerializer):
    conf_pass = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)

    class Meta:
            model = CustomUser
            fields = ['id','first_name','last_name','email','username','phone_number','password','conf_pass']

    def validate(self, attrs):
            if attrs.get('password') != attrs.get('conf_pass'):
                raise ValidationError({'password': 'Parollar bir-biriga mos kelmadi.'})
            return attrs


    def create(self, validated_data):
          validated_data.pop('conf_pass')
          user = CustomUser.objects.create_user(**validated_data)
          return user

    def to_representation(self, instance):
            data = super().to_representation(instance)
            return {
                'msg': 'signup',
                'status': status.HTTP_201_CREATED,
                'user': data
            }
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError('Username yoki parol xato')

        data['user'] = user
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = instance.get('user')
        
        refresh_token = RefreshToken.for_user(user)
        return {
            'msg': 'login',
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }

    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'photo']
        read_only_fields = ['id', 'username']


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    conf_new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('conf_new_password'):
            raise ValidationError({'new_password': 'Yangi parollar bir-biriga mos kelmadi.'})
        return attrs


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs.get('refresh')
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            raise ValidationError({'refresh': 'Yaroqsiz yoki muddati o\'tgan refresh token.'})