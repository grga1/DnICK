from django import forms
from .models import Cake

class CakeForm(forms.ModelForm):
    class Meta:
        model=Cake
        exclude=['baker']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Enter name'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter weight'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter image'
            }),

        }