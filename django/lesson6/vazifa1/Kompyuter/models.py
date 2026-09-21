from django.db import models


# Create your models here.

class Computer(models.Model):
    name = models.CharField(max_length=100)
    cpu = models.CharField(max_length=50)
    ram = models.IntegerField(help_text="GB hisobida")
    storage = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name