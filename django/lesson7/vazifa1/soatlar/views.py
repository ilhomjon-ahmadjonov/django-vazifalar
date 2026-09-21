from django.shortcuts import render, redirect, get_object_or_404
from .models import Watch
from .forms import WatchForm

def watch_list(request):
    watches = Watch.objects.all()
    return render(request, 'watch_list.html', context={'watches': watches})


def watch_detail(request, id):
    watch = get_object_or_404(Watch, id=id)
    return render(request, 'watch_detail.html', context={'watch': watch})


def watch_create(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('watch_list')
    else:
        form = WatchForm()
    return render(request, 'watch_form.html', context={'form': form, 'title': "Yangi soat qo'shish"})


def watch_update(request, id):
    watch = get_object_or_404(Watch, id=id)
    if request.method == "POST":
       
        form = WatchForm(request.POST, instance=watch)
        if form.is_valid():
            form.save()
            return redirect('watch_detail', id=watch.id)
    else:
        
        form = WatchForm(instance=watch)
    return render(request, 'watch_form.html', context={'form': form, 'title': "Soatni tahrirlash"})


def watch_delete(request, id):
    watch = get_object_or_404(Watch, id=id)
    if request.method == "POST":
        watch.delete()
        return redirect('watch_list')
    return render(request, 'watch_delete.html', context={'watch': watch})