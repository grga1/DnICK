from django import forms
from .models import Kniga

class KnigaForm(forms.ModelForm):
    class Meta:
        model = Kniga
        exclude=['slika','avtori']
        widgets={
            'naslov':forms.TextInput(attrs={
                'class':'form-control'
            }),
            'cena': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'opis': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }