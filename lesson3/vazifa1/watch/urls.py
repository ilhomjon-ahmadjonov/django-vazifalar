from django.urls import path
from .views import watch_list_create,watch_detail_update_delete
urlpatterns = [
    path('list-create/',watch_list_create),
    path('detail-update-delete/<int:pk>/',watch_detail_update_delete)

]