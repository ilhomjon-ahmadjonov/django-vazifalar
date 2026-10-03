from rest_framework import serializers
from .models import CustomUser, Verify,VIA_EMAIL,VIA_PHONE
from rest_framework.exceptions import ValidationError
from base.utils import email_or_phone_regex
class SignUpSerializer(serializers.ModelSerializer):

    phone_number_email = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','auth_status','auth_type']
        read_only_fields = fields

    def validate(self, attrs):
        phone_number_email = attrs.get('phone_number_email')
        phone_number_or_email = email_or_phone_regex(phone_number_email)

        if phone_number_email == 'email':
            data = {
                'email': phone_number_email,
                'auth_type' : VIA_EMAIL
            }

        elif phone_number_or_email == 'phone':
            data = {
                'phon_number':phone_number_email,
                'auth_type': VIA_PHONE
            }
        else:
            raise ValidationError('Telefon yoki email xato (s)')

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        if validated_data['auth_type'] == 'email':
            code = self.generated_code(validated_data['auth_type'])

            # send_code(validated_data['email'], code)

        elif validated_data['auth_type'] == 'phone':
            code = self.generated_code(validated_data['auth_type'])
                    
            # send_code(validated_data['email'], code)

        return user

    def to_representation(self, instance):
        data = super().to_representation(self, instance)
        token = instance.token()

        return{
            'data': data,
            'token': token
        }
        