from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractUser
 
# Create your models here.

class CustomUser(BaseModel, AbstractUser):
    user_role = models.CharField(max_length=50)
    auth_type = models.CharField(max_length=50)
    auth_status = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13,unique = True,null=True,blank=True)
    email = models.EmailField(max_length=255,unique = True,null=True,blank=True)
    photo = models.ImageField(upload_to='account/',blank=True,null=True)



    