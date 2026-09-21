from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer


def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'computer_list.html', context={'computers': computers})


def computer_detail(request, id):
    computer = get_object_or_404(Computer, id=id)
    return render(request, 'computer_detail.html', context={'computer': computer})


def computer_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        cpu = request.POST.get('cpu')
        ram = request.POST.get('ram')
        storage = request.POST.get('storage')
        price = request.POST.get('price')
        description = request.POST.get('description')
        
        if name:  
            Computer.objects.create(
                name=name, cpu=cpu, ram=ram, 
                storage=storage, price=price, description=description
            )
            return redirect('computer_list')
            
    return render(request, 'computer_create.html')

def computer_delete(request, id):
    computer = get_object_or_404(Computer, id=id)
    if request.method == "POST":
        computer.delete()
        return redirect('computer_list')
    return render(request, 'computer_delete.html', context={'computer': computer})