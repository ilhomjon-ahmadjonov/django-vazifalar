from django.db import models
from django.lesson5.vazifa.baseapp.models import BaseModel
from django.lesson5.vazifa.accounts.models import CustomUser
# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=123)
    desc = models.CharField(max_length=123)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, blank=True,null=True, related_name='children')
    image = models.ImageField(upload_to='catigories/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Color(BaseModel):
    name = models.CharField(max_length=150)



    def __str__(self):
        return self.name

class Size(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Product(BaseModel):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=120)
    short_desc = models.CharField(max_length=120)
    desc = models.TextField()
    info = models.TextField()
    image = models.ImageField(upload_to='products/')
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')


    def __str__(self):
        return self.title

class Banner(BaseModel):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50,default='Shop Now')
    category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title