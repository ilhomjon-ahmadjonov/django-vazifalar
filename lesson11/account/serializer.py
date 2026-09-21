from rest_framework import serializers,status
from .models import Account
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

class SignUpSerializer(serializers.ModelSerializer):
    conf_pass = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ['id','email','name','phone','password','conf_pass']

    def create(self, validated_data):
        validated_data.pop('conf_pass')
        user = Account.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'msg': 'signup',
            'status': status.HTTP_201_CREATED,
            'user': data
        }

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(username=email, password=password)
        if user is None:
            raise ValidationError('Email yoki parol xato')

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
            model = Account
            fields = ['id','email','name','phone']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields  = ['email','name','phone','date_of_birth']

    def update(self, instance, validated_data):
        if validated_data.get('email'):
            current_user = Account.objects.filter(email= validated_data.get('email')).first()
            if current_user:
                raise ValidationError('Bu email mavjud')

            instance.email = validated_data.get('email')

        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)

        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return{
            'msg':'User updated',
            'user': data
        }

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Eski parol noto'g'ri.")
        return value

    def validate(self, attrs):
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({"new_password": "Yangi parol eskisi bilan bir xil bo'lmasligi kerak."})
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password2": "Parollar mos kelmadi."})
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()


        tokens = OutstandingToken.objects.filter(user=user)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)

        return user
    
    def to_representation(self, instance):
        return {
            "msg": "Parol muvaffaqiyatli o'zgartirildi." 
        }