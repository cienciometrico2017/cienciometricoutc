from django import forms
from apps.Formacion_Academica.models import formacion_academica

class FormacionAform (forms.ModelForm):
    class Meta:
        model=formacion_academica
        fields=[
            'Nivel_Estudios',
            'NombreTitulo',
            'Fecha_Fin_Estudios',
            'Nombre_Centro_Estudios',
            'user'
        ]
        labels={
            'Nivel_Estudios':'Nivel_Estudios' ,
            'NombreTitulo':'Nombre del titulo',
            'Fecha_Fin_Estudios' :'Fecha_Fin_Estudios',
            'Nombre_Centro_Estudios':'Nombre_Centro_Estudios',
            'user': '',
        }

        widgets = {
            'Nivel_Estudios':forms.Select(attrs={'class':'form-control'}),
            'NombreTitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Fecha_Fin_Estudios':forms.DateInput(attrs={'class':'form-control datepicker', 'type':'date'}),
            'Nombre_Centro_Estudios':forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'user'}),

        }
