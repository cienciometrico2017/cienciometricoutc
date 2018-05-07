from django import forms
from apps.Articulos_Cientificos.models import articulos_cientificos

class articuloform(forms.ModelForm):
    class Meta:
        model=articulos_cientificos
        fields=[
            'titulo',
            'anio',
            'estado',
            'iSSN',
            'url',
            'doi',
            'fechaPublicacion',
            'ciudad',
            'baseDatos',
            'revista',
            'volumen',
            'numero',
            'lineaInves',
            'SubLinea',
            'resumen',
            'palabraClave',
            'documento',
            'tipoArticulo',
            'gradoAutoria',
            'aprobado',
            'user',
        ]
        labels={
            'titulo':'Título del Artículo',
            'anio':'Año',
            'estado':'Estado',
            'iSSN':'ISSN',
            'url':'Url dónde se encuentra la revista',
            'doi':'Doi dónde se encuentra la revista',
            'fechaPublicacion':'Fecha de publicación del artículo',
            'ciudad':'Ciudad donde se público el artículo',
            'baseDatos':'Base de Datos donde esta indexada la Revista',
            'revista':'Revista del artículo',
            'volumen':'Volumen de la Revista',
            'numero':'Número de la Revista',
            'lineaInves':'Linea de investigación',
            'SubLinea':'SubLinea de investigación',
            'resumen':'Resumen',
            'palabraClave':'Palabras Claves',
            'documento':'Adjuntar Archivo',
            'tipoArticulo':'Tipo de artículo',
            'gradoAutoria':'Grado de autoría',
            'aprobado':'Aprobado por',
            'user': '',
        }
        widgets={

            'Nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Estado':forms.TextInput(attrs={'class':'form-control'}),
            'Anio':forms.TextInput(attrs={'class':'form-control'}),
            'ISSN':forms.TextInput(attrs={'class':'form-control'}),
            'Base_Datos':forms.TextInput(attrs={'class':'form-control'}),
            'Url':forms.URLInput({'required':False}),
            'Fecha_Publicacion':forms.DateInput(format='%d/%m/%y', attrs={'class':'datepicker'}),
            'investigador': forms.Select(attrs={'class': 'form-control','id':'investigador'}),
            'pais': forms.Select(attrs={'class': 'form-control', 'id':'pais'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'revista': forms.Select(attrs={'class': 'form-control','id':'revista'}),
            'Resumen':forms.TextInput(attrs={'class':'form-control'}),
            'PalabrasClaves':forms.TextInput(attrs={'class':'form-control','id':'tags','placeholder':'Palabras Claves'}),

            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'anio':forms.NumberInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'iSSN':forms.TextInput(attrs={'class':'form-control'}),
            'url':forms.URLInput(attrs={'class':'form-control'}),
            'doi':forms.URLInput(attrs={'class':'form-control'}),
            'fechaPublicacion':forms.DateInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'baseDatos':forms.Select(attrs={'class':'form-control'}),
            'revista':forms.Select(attrs={'class':'form-control'}),
            'volumen':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'lineaInves':forms.Select(attrs={'class':'form-control'}),
            'SubLinea':forms.Select(attrs={'class':'form-control'}),
            'resumen':forms.Textarea(attrs={'class':'form-control'}),
            'palabraClave':forms.Select(attrs={'class':'form-control'}),
            'documento':forms.FileInput(attrs={'class':'form-control'}),
            'tipoArticulo':forms.TextInput(attrs={'class':'form-control'}),
            'gradoAutoria':forms.TextInput(attrs={'class':'form-control'}),
            'aprobado':forms.TextInput(attrs={'class':'form-control'}),
            'user': forms.HiddenInput(attrs={'class': 'form-control', 'id': 'user'}),
         }