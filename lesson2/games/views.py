from django.shortcuts import render, get_object_or_404
from .models import Game
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.decorators import api_view

@api_view(['POST'])
def game_create(request):
    title = request.data.get('title')
    genre = request.data.get('genre')
    price = request.data.get('price')

    Game.objects.create(title=title,genre=genre,price=price)

    return Response({
        'msg': "Game created"
    },
      status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
def game_list(request):
     games = Game.objects.all()

     response = []
     for game in games:
          data = {}
          data['title'] = game.title
          data['genre'] = game.genre
          data['price'] = game.price
          response.append(data)

     return Response({
          'msg': "Game list",
          'count': len(response),
          'game': response 
     },
       status=status.HTTP_200_OK
     )

@api_view(['GET'])
def game_detail(request,pk):
     game = get_object_or_404(Game,pk=pk)

     data = {
          'id': game.id,
          'title': game.title,
          'genre': game.genre,
          'price': game.price

     }
     return Response({
          'msg': "Game detail",
          'game': data
     },
        status=status.HTTP_200_OK
     )

@api_view(['PUT'])
def game_update(request,pk):
     game = Game.objects.filter(pk=pk).first()
     if game is None:
          raise NotFound(detail= 'Game not found')

     title = request.data.get('title')
     genre = request.data.get('genre')
     price = request.data.get('price')

     game.title=title
     game.genre=genre
     game.price=price
     game.save()
     return Response({
          'msg': "Game updated",
          'title': game.title,
          'genre': game.genre,
          'price': game.price
     },
        status=status.HTTP_200_OK
     )


@api_view(['PATCH'])
def game_p_update(request,pk):
     game = Game.objects.filter(pk=pk).first()
     if game is None:
          raise NotFound(detail='Game not found')

     title = request.data.get('title')
     genre = request.data.get('genre')
     price = request.data.get('price')

     if title:
          game.title=title
     if genre:
          game.genre=genre
     if price:
          game.price=price
     game.save()

     return Response({
          'msg': "Game partial updated",
          'title': game.title,
          'genre': game.genre,
          'price': game.price
     },
       status=status.HTTP_200_OK
     )
@api_view(['DELETE'])
def game_delete(request,pk):
     game = get_object_or_404(Game,pk=pk)
     game.delete()

     return Response({
          'msg': "Game Delete"
     },
       status=status.HTTP_200_OK
     )