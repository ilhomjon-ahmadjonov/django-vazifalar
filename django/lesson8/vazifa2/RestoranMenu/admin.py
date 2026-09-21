from django.contrib import admin
from .models import Chef,Category,Product
# Register your models here.
admin.site.register(Chef)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmoin(admin.ModelAdmin):
    search_fields= ['name','price']
    list_filter= ['chef', 'category']