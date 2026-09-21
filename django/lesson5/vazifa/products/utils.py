from .models import Product,Category
from django.db.models import Count

def get_products():
    return Product.objects.all().order_by('-created_at')

def get_categories():
    return Category.objects.all().order_by('-created_at')

def get_category_child():
    return [category for category in get_categories() if category.children.exists()]

def get_category_not_child():
    return [category for category in get_categories() if not category.children.exists()]

def get_products_by_category(category):
    return category.products.all().order_by('-created_at')

def get_discount_products():
    return Product.objects.all().order_by('-discount')

def get_product_with_category_products(product):
    category = product.category
    return category.products.exclude(product=product).order_by('-created_at')

def get_product_ordering():
    return Product.objects.annotate(order_count=Count('product_orders')).order_by('-order_count')