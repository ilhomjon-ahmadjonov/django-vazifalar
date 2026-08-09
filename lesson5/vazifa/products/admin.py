from django.contrib import admin
from .models import Product, Category, Color, Size, Banner

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'quantity', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['title', 'short_desc']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Banner)
