from rest_framework import serializers, status
from .models import Movie

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'