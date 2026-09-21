from django.shortcuts import render,get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def product_create(request):
    title = request.data.get('title')
    desc = request.data.get('desc')
    price = request.data.get('price')

    Product.objects.create(title=title,desc=desc,price=price)

    return Response({
        "msg": 'product created'
    },status=status.HTTP_201_CREATED)

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()

    response = []
    for product  in products:
        data = {}
        data['title'] = product.title
        data['desc']=