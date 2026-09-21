from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','year']


        def clean_password(self):
            password = self.clean_data.get('password')


            if len(password) < 8:
                raise ValidationError('Parollar kamida 8 ta belgidan iborat bolishi kerak')
            
            return password
        
        def clean(self):
            data = super().clean()
            password = data.get('password') 
            confirm_password = data.get("confirm_password")

            if password and confirm_password and password != confirm_password:
                raise ValidationError("Parollar mos emas")
            

class LoginForm(forms.Form):
    username =forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileUpdateForm(forms.ModelForm):
    model = CustomUser()
    fields = ['first_name','last_name','email','username','year']