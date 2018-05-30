from django.shortcuts import render, HttpResponseRedirect
from apps.perfiles.models import Perfil
from apps.roles.models import Rol
from apps.zona.models import zona
# Create your views here.

def inicio(request):
    zona1= zona.objects.all()



    return render(request, 'base1/inicio.html', { 'zona':zona1})


def Graficas(request):
    zona1 = zona.objects.all()

    return render(request, 'base/Graficas.html', {'zona': zona1})
