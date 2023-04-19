from django import forms
from .models import Students


class Studentform(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control'}),
            'physics': forms.NumberInput(attrs={'class': 'form-control'}),
            'chemistry': forms.NumberInput(attrs={'class': 'form-control'}),
            'maths': forms.NumberInput(attrs={'class': 'form-control'}),
            'computer_science': forms.NumberInput(attrs={'class': 'form-control'}),
        }
