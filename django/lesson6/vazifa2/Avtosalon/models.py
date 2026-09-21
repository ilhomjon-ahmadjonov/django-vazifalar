from django.db import models

class Car(models.Model):
    brand_name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField(help_text="km hisobida")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    fuel_type = models.CharField(max_length=50)

    def __str__(self):
        return self.brand_name