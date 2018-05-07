from django import forms

from apps.Libro.models import libro


class DocumentForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = [
            'Titulo',
            'ISBN',
            'Anio',
            'Editorial',
            'Resumen',
            'PalabrasClave',
            'Documento',
            'BaseDatos',
            'Url',
            'Doi',
            'UbicacionFisica',
            'capitulo',
            'gradoAutoria',
            'user',
        ]
        labels = {
            'Titulo': 'Título del Libro',
            'ISBN': 'ISBN',
            'Anio': 'Año de publicación',
            'Editorial': 'Editorial',
            'Resumen': 'Resumen del Libro',
            'PalabrasClave': 'Palabras Claves',
            'Documento': 'Adjuntar Archivo',
            'BaseDatos': 'Base de datos',
            'Url': 'URL',
            'Doi': 'Doi',
            'UbicacionFisica': 'Ubicación Física del Libro',
            'capitulo': 'Capítulo de libro',
            'gradoAutoria': 'Grado de autoria',
            'user': '',
        }

        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ISBN': forms.TextInput(attrs={'class': 'form-control'}),
            'Anio': forms.TextInput(attrs={'class': 'form-control'}),
            'Editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'Resumen': forms.Textarea(attrs={'class': 'form-control'}),
            'PalabrasClave': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'tags', 'placeholder': 'Palabras Claves'}),
            'Documento': forms.FileInput({'required': False}),
            'BaseDatos': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'tags', 'placeholder': 'Palabras Claves'}),
            'Url': forms.URLInput(attrs={'class': 'form-control'}),
            'Doi': forms.URLInput(attrs={'class': 'form-control'}),
            'UbicacionFisica': forms.TextInput(attrs={'class': 'form-control'}),
            'capitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'gradoAutoria': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id':'user'}),
        }
