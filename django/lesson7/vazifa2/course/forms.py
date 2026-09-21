from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'mentor', 'duration_months', 'price']


    def clean_duration_months(self):
        duration = self.cleaned_data.get('duration_months')
        if duration is not None and (duration < 1 or duration > 12):
            raise forms.ValidationError("Kurs davomiyligi 1 va 12 oy oralig'ida bo'lishi shart!")
        return duration


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Kurs narxi manfiy bo'lishi mumkin emas!")
        return price