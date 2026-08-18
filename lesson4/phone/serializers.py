from rest_framework import serializers,status
from .models import Phone

class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'