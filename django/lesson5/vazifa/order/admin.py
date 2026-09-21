from django.contrib import admin
from .models import Card, CardItem, Order, OrderItem

admin.site.register(Card)
admin.site.register(CardItem)
admin.site.register(Order)
admin.site.register(OrderItem)
