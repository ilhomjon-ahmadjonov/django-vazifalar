from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('<int:id>/', views.car_detail, name='car_detail'),
    path('create/', views.car_create, name='car_create'),
    path('<int:id>/delete/', views.car_delete, name='car_delete'),
]