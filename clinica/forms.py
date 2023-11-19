from django import forms
from .models import Medico
from .models import citaMedica
from django.core.exceptions import ValidationError


class MedicoForm(forms.ModelForm):

    def clean_anos_experiencia(self):
        anos_experiencia = self.cleaned_data.get('anos_experiencia')
        if anos_experiencia is not None and anos_experiencia < 0:
            raise ValidationError("Los años de experiencia no pueden ser negativos")
        return anos_experiencia

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



class CitaForm(forms.ModelForm):

    class Meta:
        model = citaMedica
        fields = [
            'medico',
            'paciente',
            'fecha',
            'hora',
            'centro',
        ]
        labels = {
            'medico': 'Medico',
            'paciente': 'Paciente',
            'fecha': 'Fecha',
            'hora': 'Hora',
            'centro': 'Centro',
        }
        widgets = {
            'medico': forms.Select(attrs={'class':'form-control'}),
            'paciente': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class':'form-control', 'type': 'time'}),
            'centro': forms.Select(attrs={'class':'form-control'}),
        }