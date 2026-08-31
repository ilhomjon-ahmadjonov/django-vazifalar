from django.shortcuts import render
from .serializer import ProductSerializer
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework.exceptions import ValidationError
from account.permissions import IsAdmin


class ProductCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(user=request.user,**serializer.validated_data)

        return Response({
            'msg' : 'Product created successfully!',
            "product" : ProductSerializer(product).data
        }, status=201)





class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
            car = Product.objects.all()
            serializer =ProductSerializer(car,many=True)
    
            return Response({
                'msg': "Car list",
                'count': len(car),
                'car': serializer.data
            },
                status=status.HTTP_200_OK
            )

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        if request.user != product.user:
            raise ValidationError(detail='siz product egasimasiz')
        serializer = ProductSerializer(product)
        return Response({
            'msg': "Product detail",
            'product': serializer.data
        },
            status=status.HTTP_200_OK
        )


class ProductUpdateAPIView(APIView):
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg" : "Product updated successfully!",
            "product" : serializer.data
        }, status=200)



class ProductPartialUpdateAPIView(APIView):
    def patch(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(data=request.data, instance=product, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg" : "Product partially updated successfully!",
            "product" : serializer.data
        }, status=200)



class ProductDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({
            "msg" : "Product deleted successfully!"
        }, status=204)

