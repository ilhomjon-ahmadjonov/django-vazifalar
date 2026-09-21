from django.db import models

class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) # max_digits aniq belgilandi
    is_indoor = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.color})"