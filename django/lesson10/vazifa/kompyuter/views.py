from django.shortcuts import render
from .models import Computer
from django.lesson10.vazifa.kompyuter.views import View
from .forms import CreateComputerForm

# Create your views here.
class ComputerList(View):
    def get(self,request):
        computer = Computer.objects.all()
        return render(request,'list.html',context={'computer':computer})

class ComputerCreate(View):
    def get(self,request):
        form = CreateComputerForm()
        return render(request,'create.html', context={'form':form})

    def post(self,request):
        form = CreateComputerForm()



class ComputerUpdate(View):
    def get(self,request):
 