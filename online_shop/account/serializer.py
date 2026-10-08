from rest_framework import serializers
from .models import CustomUser, Verify,VIA_EMAIL,VIA_PHONE
from rest_framework.exceptions import ValidationError
from base.utils import email_or_phone_regex, send_code
class SignUpSerializer(serializers.ModelSerializer):

    phone_number_email = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','auth_status','auth_type','phone_number_email']
        read_only_fields = fields

    def validate(self, attrs):
        phone_number_email = attrs.get('phone_number_email')
        phone_number_or_email = email_or_phone_regex(phone_number_email)

        if phone_number_or_email == 'email':
            data = {
                'email': phone_number_email,
                'auth_type' : VIA_EMAIL
            }

        elif phone_number_or_email == 'phone':
            data = {
                'phone_number':phone_number_email,
                'auth_type': VIA_PHONE
            }
        else:
            raise ValidationError('Telefon yoki email xato (s)')

        return data

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.save()
        
        if validated_data['auth_type'] == VIA_EMAIL:
            code = user.generate_code(validated_data['auth_type'])
            print(f'CODE EMAIL: {code} =========================')
            send_code(validated_data['email'], code)

        elif validated_data['auth_type'] == VIA_PHONE:
            code = user.generate_code(validated_data['auth_type'])
            print(f'CODE PHONE: {code} =========================')        
            # send_code(validated_data['email'], code)

        else:
            raise ValidationError('Email yoki telefon raqam xato')

        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        token = instance.token()

        return{
            'data': data,
            'token': token
        }
