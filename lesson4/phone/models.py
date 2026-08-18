from django.db import models

# Create your models here.
class Phone(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.brand
