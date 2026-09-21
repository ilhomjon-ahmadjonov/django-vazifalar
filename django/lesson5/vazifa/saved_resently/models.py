from django.db import models
from django.lesson5.vazifa.products.models import Product
from django.lesson5.vazifa.accounts.models import CustomUser
from django.lesson5.vazifa.baseapp.models import BaseModel
# Create your models here.


class Saved(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    class Meta:
        unique_together = {'user','product'}