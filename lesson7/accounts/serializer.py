from rest_framework import serializers
from .models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','first_name','last_name','email','phone_number','photo','username','password']