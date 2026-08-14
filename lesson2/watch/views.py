from django.shortcuts import render ,get_object_or_404
from .models import Watch
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def watch_create(request):
    name = request.data.get('name')
    desc = request.data.get('desc')
    price = request.data.get('price')

    Watch.objects.create(name=name,desc=desc,price=price)

    return Response({
        'msg': "Watch created"
    },
       status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
def watch_list(request):
    watches = Watch.objects.all()
    res = []
    for watch in watches:
        data = {}
        data['name'] = watch.name
        data['desc'] = watch.desc
        data['price'] = watch.price
        res.append(data)

    return Response({
        'msg': "watch created",
        'count': len(res),
        'watch' :  res
    },
       status=status.HTTP_200_OK
    )

@api_view(['GET'])
def watch_detail(request,pk):
    watch = get_object_or_404(Watch,pk=pk)
    data = {
        'id': watch.id,
        'name': watch.name,
        'desc': watch.desc,
        'price': watch.price
    }

    return Response({
        'msg': "Watch detail",
        'watch': data
    },
       status=status.HTTP_200_OK
    )

@api_view(['PUT'])
def watch_update(request,pk):
    watch = Watch.objects.filter(pk=pk).first()
    if watch is None:
        raise NotFound(detail='Watch not found')

    name = request.data.get('name')
    desc = request.data.get('desc')
    price = request.data.get('price')

    watch.name=name
    watch.desc=desc
    watch.price=price
    watch.save()

    return Response({
        'msg': "Watch updated",
        'name': watch.name,
        'desc': watch.desc,
        'price': watch.price
    },
      status=status.HTTP_200_OK
    )

@api_view(['PATCH'])
def watch_p_update(request,pk):
    watch = Watch.objects.filter(pk=pk).first()
    if watch is None:
        raise NotFound(detail='Watch not found')

    name = request.data.get('name')
    desc = request.data.get('desc')
    price = request.data.get('price')
    if name:
     watch.name=name
    if desc:
     watch.desc=desc
    if price:
     watch.price=price
    watch.save()

    return Response({
        'msg': "Watch partial updated",
        'name': watch.name,
        'desc': watch.desc,
        'price': watch.price
    },
      status=status.HTTP_200_OK
    )

@api_view(['DELETE'])
def watch_delete(request,pk):
   watch = get_object_or_404(Watch,pk=pk)
   watch.delete()

   return Response({
      'msg': "Watch delete"
   },
    status=status.HTTP_200_OK
   ) 