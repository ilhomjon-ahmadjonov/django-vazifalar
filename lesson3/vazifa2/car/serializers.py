from rest_framework import serializers,status
from .models import Car
from rest_framework.exceptions import ValidationError

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'