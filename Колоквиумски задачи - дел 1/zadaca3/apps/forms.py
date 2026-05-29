from  django import forms
from .models import Izlozba

class IzlozbaForm(forms.ModelForm):
    class Meta:
        model = Izlozba
        exclude=['tourGuide']
        widgets = {
            'naslov':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'
            }),
            'datumNaPocetok': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Destination'
            }),
            'datumNaZavrsuvanje': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            'lokacija': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Length of trip'
            }),
            'opis': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Length of trip'
            }),
        }