from django.shortcuts import render
from .serializers import FoodSerializers
from .models import Food
from rest_framework.generics import GenericAPIView,get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class FoodListView(GenericAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializers

    def get(self,request):
       food = self.get_queryset()
       page_size = 3
       q = request.query_params.get('q')
       price = request.query_params.get('price')
       pagee = int(request.query_params.get('page'))
       if q:
           food = food.filter(name__icontains=q)

       if price:
           food = food.filter(price__lte=float(price))

       if pagee:
           page = int(pagee)
           food =  food[(page-1)*page_size: page*page_size]

       serializer = self.get_serializer(food,many=True)


       return Response({
            'msg': "Food list",
            'count': food.count(),
            'food': serializer.data
        },
            status=status.HTTP_200_OK
        )

    