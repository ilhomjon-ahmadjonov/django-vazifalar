from django.shortcuts import render ,get_object_or_404
from .models import Watch
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .serializers import WatchSerializer
# Create your views here.

@api_view(['POST','GET'])
def watch_list_create(request):

    if request.method == 'POST':
        serializer = WatchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Watch created",
            'watch': serializer.data
        },
           status=status.HTTP_201_CREATED
        )

    if request.method == 'GET':
        watch = Watch.objects.all()
        serializer = WatchSerializer(watch, many=True)


        return Response({
            'msg': 'Watch list',
            'count': len(watch),
            'watch': serializer.data
        },
        status=status.HTTP_200_OK
        )

@api_view(['GET','PUT','PATCH','DELETE'])
def watch_detail_update_delete(request,pk):
    watch = Watch.objects.filter(pk=pk).first()
    if watch is None:
        raise NotFound(detail="Watch not found")

    if request.method == 'GET':
        serializer = WatchSerializer(watch)


        return Response({
            'msg': "Watch detail",
            'watch': serializer.data
        },
          status=status.HTTP_200_OK
        )

    if request.method == 'PUT':
        serializer = WatchSerializer(instance=watch, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
                'msg': "Watch updated",
                'watch': serializer.data
            },
              status=status.HTTP_200_OK
            )


    if request.method == 'PATCH':
        serializer = WatchSerializer(instance=watch, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': "Watch partial updated",
            'watch': serializer.data
        },
            status=status.HTTP_200_OK
        )

    if request.method == 'DELETE':
        watch.delete()

        return Response({
            'msg': "Watch deleted",
        },
            status=status.HTTP_200_OK
        )