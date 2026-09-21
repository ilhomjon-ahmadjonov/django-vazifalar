from django.urls import path
from . import views

urlpatterns = [
    path('', views.watch_list, name='watch_list'),
    path('<int:id>/', views.watch_detail, name='watch_detail'),
    path('create/', views.watch_create, name='watch_create'),
    path('<int:id>/update/', views.watch_update, name='watch_update'),  
    path('<int:id>/delete/', views.watch_delete, name='watch_delete'),
]