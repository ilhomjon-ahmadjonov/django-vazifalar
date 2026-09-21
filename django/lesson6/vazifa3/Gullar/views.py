from django.shortcuts import render, redirect, get_object_or_404
from .models import Flower

def flower_list(request):
    flowers = Flower.objects.all()
    return render(request, 'flower_list.html', {'flowers': flowers})

def flower_detail(request, id):
    flower = get_object_or_404(Flower, id=id)
    return render(request, 'flower_detail.html', {'flower': flower})

def flower_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        color = request.POST.get('color')
        price = request.POST.get('price')
        is_indoor = request.POST.get('is_indoor') == 'on'
        description = request.POST.get('description')
        
        if name:
            Flower.objects.create(
                name=name, color=color, price=price,
                is_indoor=is_indoor, description=description
            )
            return redirect('flower_list')
    return render(request, 'flower_create.html')

def flower_delete(request, id):
    flower = get_object_or_404(Flower, id=id)
    if request.method == "POST":
        flower.delete()
        return redirect('flower_list')
    return render(request, 'flower_delete.html', {'flower': flower})