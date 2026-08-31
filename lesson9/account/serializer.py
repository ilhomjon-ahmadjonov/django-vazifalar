from rest_framework import serializers,status
from .models import Customuser
from rest_framework.exceptions import ValidationError

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    conf_pass = serializers.CharField(write_only=True)
    class Meta:
        model = Customuser 
        fields =  ['id','first_name','last_name','email','username','phone_number','photo','password','conf_pass']

    def validate(self, data):
        password = data.get('password')
        conf_pass = data.get('conf_pass')

        if password and conf_pass and password != conf_pass:
            raise ValidationError('parollar mos emas')

   
    def validated_data(self):
        return super().validated_data

        