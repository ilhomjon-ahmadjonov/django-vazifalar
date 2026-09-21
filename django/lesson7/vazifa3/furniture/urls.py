from django.urls import path
from . import views

urlpatterns = [
    path('', views.furniture_list, name='furniture_list'),
    path('<int:id>/', views.furniture_detail, name='furniture_detail'),
    path('create/', views.furniture_create, name='furniture_create'),
    path('<int:id>/update/', views.furniture_update, name='furniture_update'),
    path('<int:id>/delete/', views.furniture_delete, name='furniture_delete'),
]