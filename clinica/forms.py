from django import forms
from .models import Medico
from .models import citaMedica
from django.core.exceptions import ValidationError
from datetime import datetime, time, date



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
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < date.today():
            raise forms.ValidationError("La fecha no puede ser anterior a hoy.")
        return fecha
    
    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        now = datetime.now().time()

        if hora < now:
            raise forms.ValidationError("La hora no puede ser anterior a la hora actual.")
        return hora

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