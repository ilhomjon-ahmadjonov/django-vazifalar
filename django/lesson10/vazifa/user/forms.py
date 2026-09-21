from django import forms
from .models import Customuser
from django.core.exceptions import ValidationError

class RForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customuser
        fields = ['first_name','last_name','username','phone_number','year','password','confirm_password']


    def clean_password(self):
                password = self.cleaned_data.get('password')

                if len(password) < 8:
                       raise ValidationError("Parol kamida 8 ta belgidan iborat bolishi kerek")



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        fields = ['last_name','first_name','username','year']
        model = Customuser()