from django.db import models

# Create your models here.

class Furniture(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    is_avialable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural ="Furniture"
        db_table = "furniture"

