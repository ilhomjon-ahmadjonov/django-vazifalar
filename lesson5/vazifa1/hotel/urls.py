from django.urls import path
from .views import *

urlpatterns = [
    path('list/', HotelListCreateView.as_view()),
    path('create/', HotelCreateView.as_view()),
    path('update/<int:pk>/', HotelUpdateView.as_view()),
     path('delete/<int:pk>/', HotelDeleteView.as_view()),

]