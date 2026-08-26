from rest_framework import serializers,status
from .models import Customuser
from rest_framework.exceptions import ValidationError

class Signupserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    conf_pass = serializers.CharField(write_only=True)
    class Meta:
        model = Customuser
        fields = ['id','first_name','last_name','email','username','phone_number','photo','password','conf_pass']

    def validate(self, data):
        password = data.get('password')
        conf_pass = data.get('conf_pass')

        if password and conf_pass and password != conf_pass:
            raise ValidationError('Parollar mos emas')
        return data

    def validate_username(self,username):
        if username[0].isdigit():
            raise ValidationError('Username raqam bilan boshlanmasin')

        return username

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id','first_name','last_name','email','username','phone_number','photo']


class ProfileUpdateSerializer(ProfileSerializer):
    id = serializers.CharField(read_only=True)

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    conf_password = serializers.CharField()

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        conf_password = attrs.get('conf_password')

        if conf_password and new_password and conf_password != new_password:
            raise ValidationError(detail='Yangi oarollar mos emas')

        if new_password and old_password and new_password == old_password:
            raise ValidationError(detail='Yangi parol eskisiga teng bolmasin')

        return attrs