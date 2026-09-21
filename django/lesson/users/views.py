from django.shortcuts import render,redirect
from .models import CustomUser
from django.views import View
from .forms import RegisterForm
from django import forms
from .forms import LoginForm
from django.contrib.auth import authenticate,login
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    return render(request,'home.html')


class RegisterView(View):
    def get(self, request):
        return render(request,'auth/register.html')
    
    def post(self,request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        year = request.POST.get('year')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # user = CustomUser.objects.create(
        #     username=username,
        #     first_name=first_name,
        #     year=year,
        #     password=password,
        # )
        # return redirect('home')
        
        
        CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            year=year,
            password=password,
        )
        return redirect('home')

        # user = CustomUser(
        #     username=username,
        #     first_name=first_name,
        #     year=year,
        #     password=password,
        # )  
        # user.set_password(password)
        # user.save()
        # return redirect('home') 

class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'auth/login.html', context={'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.changed_data['username']
            password = form.changed_data['password']

            user = authenticate( username=username,password=password)
            if not user:
                raise ValidationError('parol yoki username xato')
            
            login(request, user)
            return redirect('home')