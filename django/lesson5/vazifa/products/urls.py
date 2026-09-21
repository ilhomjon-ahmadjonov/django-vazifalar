from django.urls import path
from .views import IndexView, ShopView, ProductDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<uuid:pk>/', ProductDetailView.as_view(), name='product-detail'),
]