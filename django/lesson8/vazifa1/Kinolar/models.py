from django.db import models
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Derector(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Category(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Move(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators= [MinValueValidator(20_000), MaxValueValidator(1_500_000)])
    image = models.ImageField(upload_to='media/', default='defualt_move.jpg', validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])])
    director = models.ForeignKey(Derector, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rejisyor: {self.director.first_name} |Janr: {self.category.name}|Kino: {self.name}"