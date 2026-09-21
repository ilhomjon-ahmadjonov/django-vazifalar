from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from .utils import get_categories, get_category_child, get_category_not_child, get_product_ordering, get_products
from django.db.models import Q

# Create your views here.
class IndexView(View):
    def get(self,request):
        context = {
            'categories' : get_categories(),
            'get_category_child':get_category_child(),
            'get_category_not_child': get_category_not_child(),
            'get_product_ordering':get_product_ordering(),
            'products': get_products()
        }
        return render(request, 'index.html', context)

class ShopView(View):
    def get(self, request):
        products = Product.objects.all()
        q = request.GET.get('q')
        category_id = request.GET.get('category')
        
        if q:
            products = products.filter(Q(title__icontains=q) | Q(short_desc__icontains=q) | Q(desc__icontains=q))
        
        if category_id:
            products = products.filter(category_id=category_id)
            
        context = {
            'products': products,
            'categories': get_categories(),
        }
        return render(request, 'shop.html', context)

class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        comments = product.product_comments.all().order_by('-created_at')
        context = {
            'product': product,
            'comments': comments,
        }
        return render(request, 'detail.html', context)