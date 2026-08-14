from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.title