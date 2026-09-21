from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, CheckoutView, PlaceOrderView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<uuid:pk>/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<uuid:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
]
