from django.urls import path
from .views import watch_create,watch_list,watch_detail,watch_update,watch_p_update,watch_delete
urlpatterns = [
    path('create/',watch_create),
    path('list/',watch_list),
    path('detail/<int:pk>/',watch_detail),
    path('update/<int:pk>/',watch_update),
    path('updatep/<int:pk>/',watch_p_update),
    path('delete/<int:pk>/',watch_delete),

]