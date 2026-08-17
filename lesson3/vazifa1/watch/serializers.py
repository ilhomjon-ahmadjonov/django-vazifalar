from rest_framework import serializers,status
from .models import Watch
from rest_framework.exceptions import ValidationError


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields =  '__all__'


    def validate(self, data):
        name = data.get('name')
        if name.isdigit():
            raise ValidationError(detail='Name raqamlardan iborat bolmasin', status=status.HTTP_400_BAD_REQUEST)
        
        return data



    def validate_desc(self,value):
        if len(value) < 10:
            raise ValidationError(detail='Izoh kamida 10 ta belgidan iborat bolishi kerak', status=status.HTTP_400_BAD_REQUEST)
        return value