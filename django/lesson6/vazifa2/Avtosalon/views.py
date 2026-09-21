from django.shortcuts import render, redirect, get_object_or_404
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', context={'cars': cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'car_detail.html', context={'car': car})


def car_create(request):
    if request.method == "POST":
        brand_name = request.POST.get('brand_name')
        color = request.POST.get('color')
        year = request.POST.get('year')
        mileage = request.POST.get('mileage')
        price = request.POST.get('price')
        fuel_type = request.POST.get('fuel_type')
        
        if brand_name:
            Car.objects.create(
                brand_name=brand_name, color=color, year=year,
                mileage=mileage, price=price, fuel_type=fuel_type
            )
            return redirect('car_list')
            
    return render(request, 'car_create.html')


def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request, 'car_delete.html', context={'car': car})