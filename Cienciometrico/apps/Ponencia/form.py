from django import forms
from apps.Ponencia.models import ponencia

class PonenciaForm (forms.ModelForm):
    class Meta:
        model = ponencia
        fields = [
            'nombrePonencia',
            'lugarPonencia',
            'tituloPonencia',
            'fechaPonencia',
            'anio',
            'nivelAutoria',
            'palabrasClave',
            'resumen',
            'certificado',
            'urlPonencia',
            'financiamiento',
            'informe',
            'articuloCientifico',
            'user',

        ]
        labels = {
            'nombrePonencia':'Nombre del evento',
            'lugarPonencia':'Lugar del evento',
            'tituloPonencia':'Titulo de ponencia',
            'fechaPonencia':'Fecha de la ponencia',
            'anio':'Año',
            'nivelAutoria':'Nivel de autoría',
            'palabrasClave':'Palabras clave',
            'resumen':'Resumen',
            'certificado':'Certificado',
            'urlPonencia':'URL',
            'financiamiento':'Financiamiento',
            'informe':'Informe de actividades',
            'articuloCientifico':'Con articulo',
            'user': '',

        }
        widgets = {
            'nombrePonencia':forms.TextInput(attrs={'class': 'form-control'}),
            'lugarPonencia':forms.TextInput(attrs={'class': 'form-control'}),
            'tituloPonencia': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaPonencia':forms.DateInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivelAutoria':forms.TextInput(attrs={'class': 'form-control'}),
            'palabrasClave':forms.Select(attrs={'class': 'form-control'}),
            'resumen':forms.Textarea(attrs={'class': 'form-control'}),
            'certificado':forms.TextInput(attrs={'class': 'form-control'}),
            'urlPonencia':forms.URLInput(attrs={'class': 'form-control'}),
            'financiamiento':forms.Select(attrs={'class': 'form-control'}),
            'informe': forms.FileInput(attrs={'class': 'form-control'}),
            'articuloCientifico': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'user'}),

        }
