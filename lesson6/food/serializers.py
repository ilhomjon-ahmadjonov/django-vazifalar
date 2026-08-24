from rest_framework import serializers,status
from .models import Food


class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'