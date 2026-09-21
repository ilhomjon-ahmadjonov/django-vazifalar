from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','phone_number','year','password','confirm_password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise ValidationError("Parol kamida 8 ta belgidan iborat bolishi kerak ")
        if not any(char.isupper() for char in password):
            raise ValidationError("Parolda kamida 1 ta katta harf bolishi kerak")
        return password
    
    def clean(self):
        data = super().clean()
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password',"Parollar mos emas")
            return data
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['last_name','first_name','username','year']
        model = CustomUser()