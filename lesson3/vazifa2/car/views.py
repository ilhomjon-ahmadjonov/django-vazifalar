from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
# Create your views here.

class CarListCreateApiView(APIView):
    def get(self,request):
        car = Car.objects.all()
        serializer = CarSerializer(car,many=True)

        return Response({
            'msg': "Car list",
            'count': len(car),
            'car': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Car created",
            'car': serializer.data
        },
            status=status.HTTP_201_CREATED
        )

class CarDetaialDeleteUpdate(APIView):
    def get_object(self,request,pk):
        car = Car.objects.filter(pk=pk).first()
        if car is None:
            raise NotFound(detail='Car not found')
        return car

    def get(self,request,pk):
        car = self.get_object(request,pk)
        serializer = CarSerializer(car)

        return Response({
            'msg': "Car detail",
            'car': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def  put(self,request,pk):
        car = self.get_object(request,pk)
        serializer = CarSerializer(instance=car, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Car updated",
            'car': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def patch(self,request,pk):
        car = self.get_object(request,pk)
        serializer = CarSerializer(instance=car,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': "Car updated",
            'car': serializer.data
        },
            status=status.HTTP_200_OK
        )



    def delete(self,request,pk):
        car = self.get_object(request,pk)
        car.delete()

        return Response({
            'msg': "Car created",
        },
            status=status.HTTP_200_OK
        )


