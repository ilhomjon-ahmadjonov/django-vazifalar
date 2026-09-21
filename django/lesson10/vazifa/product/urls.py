from django.urls import path
from .views import product_create, product_list

urlpatterns = [
    path('create/', product_create),
    path('list/', product_list)
]
