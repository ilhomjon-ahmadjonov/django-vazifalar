from django.shortcuts import render
from .models import Phone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,get_object_or_404
from rest_framework.exceptions import NotFound
from .serializers import PhoneSerializers
 
# Create your views here.

class PhoneListCreateView(GenericAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializers

    def get(self,request):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response({
            'msg': "Phone list",
            'count': len(self.get_queryset()),
            'phone': serializer.data
        },
            status=status.HTTP_200_OK
        )



    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Phone created",
            'phone': serializer.data
        },
            status=status.HTTP_201_CREATED
        )
class PhoneDetailUpdateDelete(GenericAPIView):
    serializer_class = PhoneSerializers

    def get_object(self,request,pk):
        return get_object_or_404(Phone,pk=pk)
    
    def get(self,request,pk):
        serializer = self.get_serializer(self.get_object(request,pk))

        return Response({
            'msg': "Phone detail",
            'phone': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def put(self,request,pk):
        serializer = self.get_serializer(instance=self.get_object(request,pk),data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Phone updated",
            'phone': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def patch(self,request,pk):
        serializer = self.get_serializer(instance=self.get_object(request,pk),data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Phone partial updated",
            'phone': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def delete(self,request,pk):
        phone = self.get_object(request,pk)
        phone.delete()
        return Response({
            'msg': "Phone deleted",
        },
            status=status.HTTP_200_OK
        )