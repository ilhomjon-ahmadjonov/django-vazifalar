from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'user', 'title', 'description', 'price', 'created_at']