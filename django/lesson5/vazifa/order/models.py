from django.db import models
from django.lesson5.vazifa.baseapp.models import BaseModel
from django.lesson5.vazifa.accounts.models import CustomUser
from django.lesson5.vazifa.products.models import Product

class Card(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return f"{self.user.username} - Savatchasi"


class CardItem(BaseModel):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.card.user.username} -> {self.product}"


class Order(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    adress = models.CharField(max_length=120)

    @property
    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_orders')
    count = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        if self.product:
            return self.count * self.product.price
        return 0

    def __str__(self):
        return f"{self.order.id} -> {self.product}"