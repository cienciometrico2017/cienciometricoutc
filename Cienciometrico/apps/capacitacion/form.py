from django import forms
from apps.capacitacion.models import capacitacion

class CapacitacionForm (forms.ModelForm):
    class Meta:
        model = capacitacion
        fields = [
            'areaConocimiento',
            'horas',
            'institucion',
            'descripcion',
            'evidencias',
            'user',
        ]
        labels = {
            'areaConocimiento':' Área de conocimiento',
            'horas': 'Horas totales',
            'institucion': 'Insttitución',
            'descripcion': 'Descripción',
            'evidencias': 'Evidencias',
            'user':'',
        }
        widgets = {
            'areaConocimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'evidencias': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control','id':'user','name':'user'}),
        }
