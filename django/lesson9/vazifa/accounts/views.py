from django.shortcuts import render,redirect
from .models import CustomUser
from django.views import View
from .forms import RegisterForm,ProfileUpdateForm
from django import forms
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    return render(request,'home.html')


class RegisterView(View):
    def get(self, request):
        return render(request,'auth/regis.html')
    
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
        return redirect('auth:home')

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate( username=username,password=password)
            if not user:
                form.add_error(None, 'Parol yoki username xato')
            else:
                login(request, user)
                return redirect('auth:home')
            return render(request, 'auth/login.html', context={'form': form})
           
        
class ProfilView(View):
    def get(self,request):
        user = request.user
        return render(request, 'auth/profile.html', context={'user': user})
    
class ProfileUpdateView(View):
    def get(self,request):
        form = ProfileUpdateForm(instance=request.user)
        return render(request,'auth/update.html',context={'form': form})
    
    def post(self,request):
        form = ProfileUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('auth:home')
        return render(request,'auth/update.html',context={'form': form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('auth:login')