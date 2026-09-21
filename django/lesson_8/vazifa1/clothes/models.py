from django.db import models

# Create your models here.
class Clothes(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small (S)'),
        ('M', 'Medium (M)'),
        ('L', 'Large (L)'),
        ('XL', 'X-Large (XL)'),
    ]
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    size = models.CharField(max_length=20)
    color = models.CharField(max_length=70)

    def __str__(self):
        return  f"Nomi: {self.name}|Razmeri: {self.size}|Narxi: {self.price}"
    
