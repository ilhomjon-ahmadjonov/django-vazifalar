from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:id>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('<int:id>/update/', views.course_update, name='course_update'),
    path('<int:id>/delete/', views.course_delete, name='course_delete'),
]