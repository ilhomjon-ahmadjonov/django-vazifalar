from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from django.lesson5.vazifa.products.models import Product

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        text = request.POST.get('text')
        
        if text:
            Comment.objects.create(
                user=request.user,
                product=product,
                text=text
            )
            
        return redirect('product-detail', pk=pk)
