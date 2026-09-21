from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

class BaseModel(models.Model):
    createad_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Manufacturer(models.Model):
    name = models.CharField(max_length=180, verbose_name="Kompaniya/Brend nomi")
    country = models.CharField(max_length=100, verbose_name="Ishlab chiqarilgan mamlakat")
    established_year = models.PositiveIntegerField(verbose_name="Tashkil topgan yili")

    def __str__(self):
        return self.name
    

class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Kategoriya nomi")

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=150, verbose_name="Mahsulot nomi")
    desc = models.TextField(null=True, blank=True, verbose_name="Tafsiloti / Tarkibi")
    

    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(1000), MaxValueValidator(2_000_000)],
        verbose_name="Narxi"
    )
    
    image = models.ImageField(
        upload_to='products/', 
        default='product.jpg', 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        verbose_name="Mahsulot rasmi"
    )
    

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='products', verbose_name="Ishlab chiqaruvchi")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name="Kategoriya")
    
 
    is_available = models.BooleanField(default=True, verbose_name="Sotuvda/Omborda bor")

    def __str__(self):
        return f"Brend: {self.manufacturer.name} | Kategoriya: {self.category.name} | Mahsulot: {self.name}"