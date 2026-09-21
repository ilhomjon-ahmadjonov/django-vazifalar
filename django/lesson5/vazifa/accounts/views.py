from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm,ProfileUpdateForm
from django.views import View
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListView(View):
    def get(self,request):
        user = CustomUser.objects.all()
        return render(request, 'list.html', context={'user':user})
    

class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'auth/register.html', context={'form':form})

    def post(self,request):
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('auth:login.html')
        return render(request,'auth/register.html', context={'form':form})
    


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'auth/login.html',context={'form':form})
    
    def post(self,request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(self,user)
                return redirect('auth:profile')
            else:
                form.add_error(None,"Parol yoki username xato")
                return render(request,'auth/login.html',context={'form':form})

class ProfileView(View):
    def get(self,request):
        user = request.user
        return render(request,'auth/profile.html',context={'user':user})
    
class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        form = ProfileUpdateForm(instance=user)
        return render(request,'auth/update.html',context={'form':form})
    
    def post(self,request):
        user = request.user
        form = ProfileUpdateForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth:profile')
        return render(request,'auth/update.html',context={'form':form})
    
class LogOutView(View):
    def get(self,request):
        logout(request.user)
        return redirect('auth:login')

    
































    