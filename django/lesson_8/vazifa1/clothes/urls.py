from django.urls import path
from .views import home, ClothesListView,ClothesCreateView,ClothesDetailView,ClothesDeleteView,ClothesUpdateView

urlpatterns = [
    path('',home, name= 'home'),
    path('cl-list', ClothesListView.as_view(), name='list'),
    path('cl-create', ClothesCreateView.as_view(), name='create'),
    path('cl-detail/<int:id>/', ClothesDetailView.as_view(), name='detail'),
    path('cl-delete/<int:id>/', ClothesDeleteView.as_view(), name='delete'),
    path('cl-update/<int:id>/', ClothesUpdateView.as_view(), name='update')


]