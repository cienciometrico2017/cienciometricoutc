from apps.perfiles.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegistroForm(forms.ModelForm):
    class Meta:
        model= Perfil
        fields = [
            'cedula',
            'photo',
            'coordenadas',
            'telefono',
            'genero',
            'nacionalidad',
            'roles',
            'direccion',
            'categoria',
        ]
        labels = {
            'cedula': 'Cedula',
            'photo':'Fotografia',
            'direccion': '',
            'coordenadas': 'Coordenadas',
            'telefono': 'Telefono',
            'genero': 'Genero',
            'nacionalidad': 'Nacionalidad',
            'categoria': 'Categoría del docente',
            'roles': 'Roles',
        }



        widgets = {

            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'photo':forms.FileInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','id':'address1'}),
            'coordenadas': forms.TextInput(attrs={'class': 'form-control','style':'display:none','id':'latlng', 'value':'-0.917476, -78.632573'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'roles': forms.CheckboxSelectMultiple(),

        }


class UserForm (forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'is_staff',
        ]
        labels={
            'username':'username',
            'password':'password',
            'first_name':'first_name',
            'last_name':'last_name',
            'email':'email',
            'is_staff':'is_staff',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "nombre de usuario"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(),
        }