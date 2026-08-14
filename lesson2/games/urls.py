from django.urls import path
from .views import game_create,game_list,game_detail,game_update,game_p_update,game_delete
urlpatterns = [
    path('create', game_create),
    path('list',game_list ),
    path('detail/<int:pk>/', game_detail),
    path('update/<int:pk>/',game_update),
    path('updatep/<int:pk>/',game_p_update),
    path('delete/<int:pk>/',game_delete)
    
]