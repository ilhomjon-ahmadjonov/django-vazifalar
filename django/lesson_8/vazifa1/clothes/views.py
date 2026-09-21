from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Clothes
from .forms import ClothesForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

class ClothesListView(View):
    def get(self,request):
        clothes = Clothes.objects.all().order_by('-id')
        return render(request, 'list_clothes.html', context= {'clothes': clothes})
    
class ClothesCreateView(View):
    def get(self,request):
        form = ClothesForm()
        return render(request,'create_clothes.html', context={'form': form})
    
    def post(self,request):
        form = ClothesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request,'create_clothes.html', context={'form': form})

class ClothesDetailView(View):
    def get(self,request,id):
        clothes = Clothes.objects.get(id=id)
        return render(request, 'detail_clothes.html',context={'clothes':clothes})
    
class ClothesDeleteView(View):
    def get_object(self,id):
        clothes = get_object_or_404(Clothes,id=id)
        return clothes


    def get(self,request,id):
        clothes = self.get_object(id)
        return render(request,'delete_clothes.html', context= {'clothes': clothes})
    
    def post(self, request,id):
        clothes = self.get_object(id)
        clothes.delete()
        return redirect('list')
    
class ClothesUpdateView(View):
    def get_object(self,id):
        clothes = get_object_or_404(Clothes,id=id)
        return clothes


    def get(self,request,id):
        clothes = self.get_object(id)
        form = ClothesForm(instance=clothes)
        return render(request,'update_clothes.html', context= {'clothes': clothes})
    
    def post(self, request, id):
        clothes = self.get_object(id)
        form =ClothesForm(instance=clothes, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', id=clothes.id)
        return render(request, 'update_clothes.html', context={'clothes': clothes, 'form': form})
        



