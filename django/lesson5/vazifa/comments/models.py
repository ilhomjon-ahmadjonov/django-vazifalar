from django.db import models
from django.lesson5.vazifa.accounts.models import CustomUser
from django.lesson5.vazifa.products.models import Product
from django.lesson5.vazifa.baseapp.models import BaseModel

# Create your models here.

class Comment(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_comments')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_comments')
    text = models.CharField(max_length=120)
    rate = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"


