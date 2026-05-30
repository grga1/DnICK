from django import forms

from .models import Estate

class EstateForm(forms.ModelForm):
    class Meta:
     model = Estate
     exclude = ['agents']
     widgets = {
         'name': forms.TextInput(attrs={
             'class': 'form-control'
         }),
         'description': forms.TextInput(attrs={
             'class': 'form-control'
         }),
         'location': forms.TextInput(attrs={
             'class': 'form-control'
         }),
         'area': forms.NumberInput(attrs={
             'class': 'form-control'
         }),
         'saleDate': forms.DateInput(attrs={
             'class': 'form-control'
         }),
         'image': forms.FileInput(attrs={
             'class': 'form-control'
         }),
         'reserved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
         'sold': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

     }


