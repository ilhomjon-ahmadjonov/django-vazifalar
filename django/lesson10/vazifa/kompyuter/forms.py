from django import forms

class CreateComputerForm(forms.ModelForm):
    class Meta:
        fields = ['name','price']