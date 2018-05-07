from django import forms

from apps.Proyectos.models import proyecto
class DocumentForm(forms.ModelForm):
    class Meta:
        model = proyecto
        fields = [
            'titulo',
            'financiamiento',
            'montoFinanciado',
            'montorecibido',
            'integrantes',
            'resumen',
            'palabrasClaves',
            'lineaInvestigacion',
            'subLinea',
            'tipo',
            'documentos',
        ]
        labels = {
             'titulo':'Título',
             'financiamiento':'Financiamiento',
             'montoFinanciado':'Monto financiado',
             'montorecibido':'Monto recibido',
             'integrantes':'Integrantes',
             'resumen':'Resumen',
             'palabrasClaves':'Palabras Clave',
             'lineaInvestigacion':'Linea de Investigación',
             'subLinea':'SubLinea de Investigación',
             'tipo':'Tipo de Proyecto',
             'documentos':'Adjuntar rrchivo',

        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'financiamiento': forms.Select(attrs={'class': 'form-control'}),
            'montoFinanciado': forms.TextInput(attrs={'class': 'form-control'}),
            'montorecibido': forms.TextInput(attrs={'class': 'form-control'}),
            'integrantes': forms.Select(attrs={'class': 'form-control'}),
            'resumen': forms.TextInput(attrs={'class': 'form-control'}),
            'palabrasClaves': forms.Select(attrs={'class': 'form-control'}),
            'lineaInvestigacion': forms.Select(attrs={'class': 'form-control'}),
            'subLinea': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'documentos': forms.FileInput(attrs={'class': 'form-control'}),

        }
