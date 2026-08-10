from django.shortcuts import render
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['POST'])
def Product_create(request):
    title = request.data.get('title')
    desc = request.data.get('desc')
    price = request.data.get('price')

    Product.objects.create(title=title,desc=desc,price=price)

    return Response({
        'msg': 'Product created',
    }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def Product_list(request):
    products = Product.objects.all()

    response = []
    for product in products:
        data = {}
        data['title'] = product.title
        data['desc'] = product.desc
        data['price'] = product.price
        response.append(data)

    return Response({
        'msg': "Product list",
        "count": len(response),
        "products": response
    },
      status=status.HTTP_200_OK
    )

@api_view(['GET'])
def Product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)

    data = {
        'id': product.id,
        'title' : product.title,
        'desc' : product.desc,
        'price' : product.price
    }

    return Response({
        'msg':"Product detail",
        "product": data
    },status=status.HTTP_200_OK)
