from django.urls import path
from . import views

urlpatterns = [
    path('', views.computer_list, name='computer_list'),
    path('computer/<int:id>/', views.computer_detail, name='computer_detail'),
    path('computer/create/', views.computer_create, name='computer_create'),
    path('computer/<int:id>/delete/', views.computer_delete, name='computer_delete'),
]