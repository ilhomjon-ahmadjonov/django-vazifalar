from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customuser(AbstractUser):
    phone_number = models.CharField(max_length=120,null=True,blank=True)
    photo = models.ImageField(upload_to='user/',null=True,blank=True)


    def __str__(self):
        return self.username


