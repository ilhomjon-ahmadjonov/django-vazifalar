from django.db import models
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator

# Create your models here.
class BaseModel(models.Model):
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Chef(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    experience_year = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name
    
class Category(BaseModel):
    name = models.CharField(max_length=150)


    def __str__(self):
        return self.name
    

class Product(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators= [MinValueValidator(1_000), MaxValueValidator(2_000_000)])
    image = models.ImageField(upload_to='media/', default='menu.jpg', validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])
    chef = models.ForeignKey(Chef, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return f" Oshpaz: {self.chef.first_name} |Categoriyasi: {self.category.name} |Maxsulot: {self.name}"
