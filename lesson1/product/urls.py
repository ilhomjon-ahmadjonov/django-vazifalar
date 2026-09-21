from django.urls import path
from.views import product_list_create

urlpatterns = [
    path('create/', product_list_create),
    # path('list/', Product_list),
#     path('detail/<int:pk>/',Product_detail),
#     path('update/<int:pk>/',product_update),
#     path('update-patch/<int:pk>/',product_p_update),
#     path('delete/<int:pk>/',product_delete)
]