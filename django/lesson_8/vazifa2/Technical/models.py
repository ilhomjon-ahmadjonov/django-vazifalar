from django.db import models

# Create your models here.
class Technical(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True,blank=True)
    price= models.PositiveIntegerField()

    def __str__(self):
        return self.name