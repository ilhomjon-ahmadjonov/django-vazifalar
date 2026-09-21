from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    adress = models.CharField(max_length=120, null=True,blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username