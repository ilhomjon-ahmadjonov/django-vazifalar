from django.db import models
from account.models import Customuser


class Product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']

