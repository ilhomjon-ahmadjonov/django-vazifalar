# from django.shortcuts import render
# from .models import Product
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
# from rest_framework.exceptions import NotFound
# Create your views here.

# @api_view(['POST'])
# def Product_create(request):
#     title = request.data.get('title')
#     desc = request.data.get('desc')
#     price = request.data.get('price')

#     Product.objects.create(title=title,desc=desc,price=price)

#     return Response({
#         'msg': 'Product created',
#     }, status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def Product_list(request):
#     products = Product.objects.all()

#     response = []
#     for product in products:
#         data = {}
#         data['title'] = product.title
#         data['desc'] = product.desc
#         data['price'] = product.price
#         response.append(data)

#     return Response({
#         'msg': "Product list",
#         "count": len(response),
#         "products": response
#     },
#       status=status.HTTP_200_OK
#     )

# @api_view(['GET'])
# def Product_detail(request, pk):
#     product = get_object_or_404(Product,pk=pk)

#     data = {
#         'id': product.id,
#         'title' : product.title,
#         'desc' : product.desc,
#         'price' : product.price
#     }

#     return Response({
#         'msg':"Product detail",
#         "product": data
#     },status=status.HTTP_200_OK)


# @api_view(['PUT'])
# def product_update(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     if product is None:
#         raise NotFound(update= 'Product not found')

#     title = request.data.get('title')
#     desc = request.data.get('desc')
#     price = request.data.get('price')

#     product.title=title
#     product.desc=desc
#     product.price=price

#     product.save()
#     return Response({
#         'msg': "Product updated",
#         'title': product.title,
#         'desc': product.desc,
#         'price': product.price,
#     },
#        status=status.HTTP_200_OK
#     )

# @api_view(['PATCH'])
# def product_p_update(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     if product is None:
#         raise NotFound(p_update= 'Product not found')

#     title = request.data.get('title')
#     desc = request.data.get('desc')
#     price = request.data.get('price')

#     if title:
#         product.title=title
#     if desc:
#         product.desc=desc
#     if price:
#         product.price=price

#     product.save()

#     return Response({
#         'msg': "Product partial updated",
#         'title': product.title,
#         'desc': product.desc,
#         'price':product.price
#     },
#         status=status.HTTP_200_OK
#     )

# @api_view(['DELETE'])
# def product_delete(request,pk):
#     product = get_object_or_404(Product,pk=pk)
#     product.delete()

#     return Response({
#         'msg': 'Product deleted'},
#         status=status.HTTP_200_OK
        
#     )
from django.shortcuts import render, get_object_or_404
from .models import Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.decorators import api_view
# from rest_framework.generics import get_object_or_404
# from .serializers import ProductSerializer

# Create your views here.


@api_view(['POST', 'GET'])
def product_list_create(request):
    
    if request.method == 'POST':
        # serializer = ProductSerializer(data = request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        
        
        return Response({
            'msg': 'Product created',
            # 'product': serializer.data
        }, status=status.HTTP_201_CREATED)
    
    
    if request.method == 'GET':
        products = Product.objects.all()
        # serializer = ProductSerializer(products, many=True)
            
        return Response({
            'msg':'Product list',
            'count': len(products),
            # 'products': serializer.data
        },
            status=status.HTTP_200_OK
    )



# # @api_view(['POST', 'GET'])
# # def product_list_create(request):
    
# #     if request.method == 'POST':
    
# #         title = request.data.get('title')
# #         desc = request.data.get('desc')
# #         price = request.data.get('price')
        
# #         product = Product.objects.create(title=title, desc=desc, price=price)
        
# #         return Response({
# #             'msg': 'Product created'
#                 # 'product':{
#                 #     'title':product.title,
#                 #     'desc':product.desc,
#                 #     'price':product.price,
#                 # }
# #         }, status=status.HTTP_201_CREATED)
    
    
# #     if request.method == 'GET':
# #         products = Product.objects.all()
        
# #         response = []
# #         for product in products:
# #             data = {}
# #             data['id'] = product.id
# #             data['title'] = product.title
# #             data['desc'] = product.desc
# #             data['price'] = product.price
# #             response.append(data)
            
# #         return Response({
# #             'msg':'Product list',
# #             'count': len(response),
# #             'products': response
# #         },
# #             status=status.HTTP_200_OK
# #     )
    

# @api_view(['GET', 'PUT', 'PATCH', "DELETE"])
# def product_detail_update_delete(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     if product is None:
#         raise NotFound(detail='Product not found')
    
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
       
#         return Response({
#                 'msg':"Product detail",
#                 "product": serializer.data
#             },status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         serializer = ProductSerializer(instance=product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
        
#         return Response({
#             'msg':"Product updated",
#             'product': serializer.data
#         },
#             status=status.HTTP_200_OK
#                         )
        
#     if request.method == 'PATCH':        
#         serializer = ProductSerializer(instance=product, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)   
#         serializer.save()
                
#         return Response({
#             'msg':"Product partial updated",
#             'product': serializer.data
#         },
#             status=status.HTTP_200_OK
#                         )
    
    
#     if request.method == 'DELETE':
#         product.delete()
        
#         return Response(
#             {'msg': 'Product deleted'},
#             status=status.HTTP_200_OK
#         )
