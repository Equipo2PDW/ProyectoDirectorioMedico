from django import forms
from .models import Medico

class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = [
            'nombre',
            'apellido',
            'especialidades',
            'sucursales',
            'anos_experiencia',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'especialidades': 'Especialidades',
            'sucursales': 'Sucursales',
            'anos_experiencia': 'Años de experiencia',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'especialidades': forms.SelectMultiple(attrs={'class':'form-control'}),
            'sucursales': forms.SelectMultiple(attrs={'class':'form-control'}),
            'anos_experiencia': forms.NumberInput(attrs={'class':'form-control'}),
        }