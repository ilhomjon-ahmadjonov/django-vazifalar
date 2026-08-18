from django.urls import path
from . views import  PhoneListCreateView, PhoneDetailUpdateDelete

urlpatterns = [
    path('list-create/', PhoneListCreateView.as_view()),
    path('detail-update-delete/<int:pk>/', PhoneDetailUpdateDelete.as_view())
]