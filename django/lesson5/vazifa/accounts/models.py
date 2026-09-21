from django.db import models
from django.contrib.auth.models import AbstractUser
from django.lesson5.vazifa.baseapp.models import BaseModel
# Create your models here.

class CustomUser(AbstractUser):
    year = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.username

class Contact(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email = models.EmailField(max_length=220)
    phone_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name