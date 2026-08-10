from django.urls import path
from.views import Product_create,Product_list,Product_detail

urlpatterns = [
    path('create/', Product_create),
    path('list/', Product_list),
    path('detail/<int:pk>/',Product_detail)
]