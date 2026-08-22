from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import Movie
from .serializers import MoveSerializer
from rest_framework.exceptions import NotFound
from rest_framework.viewsets import ViewSet
from rest_framework.generics import get_object_or_404
# Create your views here.

class MovieCRUDView(ViewSet):
    def list(self,request):
        movie = Movie.objects.all()
        serializer = MoveSerializer(movie,many=True)
        return Response({
            'msg': "Food list",
            'count': len(movie),
            'food': serializer.data
        },
            status=status.HTTP_200_OK
        )
    
    def create(self,request):
        serializer = MoveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': "Movie created",
            'movie': serializer.data
        },
            status=status.HTTP_201_CREATED
        )
    
    def retrieve(self,request,pk=None):
        movie = get_object_or_404(Movie,pk=pk)
        serializer = MoveSerializer(movie)
        return Response({
            'msg': "Movie detail",
            'movie': serializer.data
        },
            status=status.HTTP_200_OK
        )
    def update(self,request,pk=None):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MoveSerializer(instance=movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': "Movie update",
            'movie': serializer.data
        },
            status=status.HTTP_200_OK
        )
    def partial_update(self,request,pk):
        movie = get_object_or_404(Movie, pk=None)
        serializer = MoveSerializer(instance=movie, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': "Movie update",
            'movie': serializer.data
        },
            status=status.HTTP_200_OK
        )

    def destroy(self,request,pk=None):
        movie = get_object_or_404(Movie,pk=pk)
        movie.delete()

        return Response({
            'msg': "Movie delete",
        },
            status=status.HTTP_200_OK
        )


