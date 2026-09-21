from django.shortcuts import render,redirect, get_object_or_404
from .models import Furniture
from .forms import FurnitureForm

# Create your views here.

def furniture_list(request):
    furniture = Furniture.objects.all()
    return render(request, 'furniture_list.html', context={'items': furniture})

def furniture_detail(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    return render(request, 'furniture_detail.html', context={'item': furniture})

def furniture_create(request):
    if request.method == "POST":
        form = FurnitureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('furniture_list')
    else:
        form = FurnitureForm()
    return render(request, 'furniture_create.html', context={'form': form})

def furniture_update(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == "POST":
        form = FurnitureForm(request.POST, instance=furniture)
        if form.is_valid():
            form.save()
            return redirect('furniture_detail', id=furniture.id)
    else:
        form = FurnitureForm(instance=furniture)
    return render(request, 'furniture_update.html', context={'form': form})

def furniture_delete(request, id):
    furniture = get_object_or_404(Furniture, id=id)
    if request.method == "POST":
        furniture.delete()
        return redirect('furniture_list')
    return render(request, 'furniture_delete.html', context={'item': furniture})