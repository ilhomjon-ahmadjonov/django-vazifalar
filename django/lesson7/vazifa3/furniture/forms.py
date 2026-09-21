from django import forms
from .models import Furniture

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'desc', 'price', 'material', 'color', 'stock', 'is_avialable']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 3:
            raise forms.ValidationError("maxsulot nomi kamida 3 ta harifdan iborat bolishi kere")
        return name

    # Endi bu metod to'g'ri klass ichiga kirdi!
    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Narx 0 dan katta bolish kerak")
        if price > 100_000_000:
            raise forms.ValidationError("narx juda ketta beribsizku qaytadan kiritimg bu qimmat")
        return price
