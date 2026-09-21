from django.contrib import admin
from .models import Manufacturer, Category, Product

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'established_year')
    list_display_links = ('name',)
    search_fields = ('name', 'country')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'createad_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'manufacturer', 'price', 'is_available')
    list_display_links = ('name',)
    list_filter = ('category', 'manufacturer', 'is_available')
    search_fields = ('name', 'desc')
    list_editable = ('price', 'is_available')