from django.urls import path
from . import views

urlpatterns = [
    path('', views.flower_list, name='flower_list'),
    path('<int:id>/', views.flower_detail, name='flower_detail'),
    path('create/', views.flower_create, name='flower_create'),
    path('<int:id>/delete/', views.flower_delete, name='flower_delete'),
]