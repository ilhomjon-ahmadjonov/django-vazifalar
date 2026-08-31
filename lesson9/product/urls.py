from django.urls import path
from .views import *

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='create_product'),
    path('list/', ProductListAPIView.as_view(), name='list'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update'),
     path('detail/<int:pk>/', ProductDetailAPIView.as_view(), name='detail'),
    path('partial-update/<int:pk>/', ProductPartialUpdateAPIView.as_view(), name='partial_update'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete')
]
