from rest_framework import serializers,status
from .models import Hotel

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'