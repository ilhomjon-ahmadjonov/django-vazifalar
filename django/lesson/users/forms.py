from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'username', 'year', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise ValidationError("Parol kamida 8 ta belgidan iborat bo'lishi kerak")

        if not any(char.isupper() for char in password):
            raise ValidationError("Parolda kamida 1 ta katta harf bo'lishi kerak")

        return password

    def clean(self):
       data = super().clean()
       password = data.get('password')
       confirm_password = data.get('confirm_password')

       if password and confirm_password and password != confirm_password:
        self.add_error('confirm_password', "Parollar mos emas")

        return data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
       data = super().clean()
       username = data.get('username')
       password = data.get('password')
       user = authenticate( username=username,password=password)
