from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Card, CardItem, Order, OrderItem
from products.models import Product

class CartView(LoginRequiredMixin, View):
    def get(self, request):
        card, created = Card.objects.get_or_create(user=request.user)
        items = card.items.all()
        subtotal = sum(item.product.price * item.count for item in items if item.product)
        shipping = 10 if subtotal > 0 else 0
        total = subtotal + shipping
        
        context = {
            'card': card,
            'items': items,
            'subtotal': subtotal,
            'shipping': shipping,
            'total': total,
        }
        return render(request, 'cart.html', context)

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        card, created = Card.objects.get_or_create(user=request.user)
        
        # Check if item already exists in cart
        card_item, item_created = CardItem.objects.get_or_create(card=card, product=product)
        if not item_created:
            # If it exists, just increment count
            card_item.count += 1
            card_item.save()
            
        return redirect('cart')

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        card_item = get_object_or_404(CardItem, pk=pk, card__user=request.user)
        card_item.delete()
        return redirect('cart')

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        card, created = Card.objects.get_or_create(user=request.user)
        items = card.items.all()
        
        if not items.exists():
            return redirect('cart')
            
        subtotal = sum(item.product.price * item.count for item in items if item.product)
        shipping = 10 if subtotal > 0 else 0
        total = subtotal + shipping
        
        context = {
            'items': items,
            'subtotal': subtotal,
            'shipping': shipping,
            'total': total,
        }
        return render(request, 'checkout.html', context)

class PlaceOrderView(LoginRequiredMixin, View):
    def post(self, request):
        card = get_object_or_404(Card, user=request.user)
        items = card.items.all()
        
        if not items.exists():
            return redirect('shop')
            
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        
        # Simple concat of address fields for the single address field in Order model
        full_address = f"{address1}, {address2}, {city}"
        
        # Create Order
        order = Order.objects.create(
            user=request.user,
            adress=full_address
        )
        
        # Create OrderItems and transfer from Cart
        for item in items:
            if item.product:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    count=item.count
                )
                # optionally reduce product stock here if required by logic
                
        # Clear Cart
        items.delete()
        
        # Usually redirect to a success page, but we'll redirect to shop for now
        return redirect('index')

