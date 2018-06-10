from django.shortcuts import render
from apps.perfiles.models import Perfil
from apps.zona.models import zona
from apps.universidad.models import universidad
from apps.facultad.models import facultad
from apps.carrera.models import carrera
from apps.campus.models import campus
from apps.roles.models import Rol
from django.views.generic import ListView,TemplateView

import json
import os
import psycopg2
DSN = "dbname=cienciometric user=postgres password=1945"


# Create your views here.
def inde(request):


    return render(request, 'base/inicio.html')
















def grafica(request):

# sql para consulta directa a la bd
    con = psycopg2.connect(DSN)
    libro = []  # declaramos un vector para almacenar los numeros de cedula
    a = ""
    cur = con.cursor()
    query = 'SELECT *FROM "Libro_libro";'
    cur.execute(query)
    cont = 0  # declaramos un contadorpara controlar las iserciones en el vector
    for datos in cur.fetchall():  # ejecutamos la consulta a la base de datos
        # print(datos[4])
        a = datos[2]  # guardamos en una varible el datos de la pos 4 es decir los numeros de cedula de los usuarios
        libro.insert(cont, a)  # incertamos los datosde la consuta en el vector
        cont = cont + 1
    cur.close()
    con.close()
#   escribimos el json
    ruta = {}
    ruta['UTC'] = cont+5
    ruta['UTA'] = cont
    ruta['ESPE'] = cont
    carpeta = 'C:%sworkpase_py\cienciometricoutc\Cienciometrico\static\json' % os.sep
    os.chdir(carpeta)  # esta es la linea que hace que se cambie el lugar de trabajo
    with open('data.json', 'w') as outfile:
        carpeta = 'C:%sworkpase_py\cienciometricoutc\Cienciometrico\static\json' % os.sep
        archivo = json.dump(ruta, outfile)



   #consultamos a la bd y traemos los objetos
    zon = zona.objects.all()
    uni = universidad.objects.all()
    facu=facultad.objects.all()
    carrer=carrera.objects.all()

    return render(request, 'base/Graficas.html',{'zona': zon,'universidad':uni,"facultad":facu, "carrera":carrer })





















def producc(request):


    return render(request, 'base/produccioncientifica.html')

def similar(request):
    perfil = Perfil.objects.all()
    privi = []
    for p in perfil:
        if p.roles == '3':
            privi.append(p)

    return render(request, 'base/similares.html',{'usuario': perfil})


















class BusquedaView(ListView):
    model = zona
    template_name = "base/Graficas.html"
    context_object_name = 'zona'






from django.core import serializers
from django.http import HttpResponse

class BusquedaAjaxView(TemplateView):


    def get(self,request,*args, **kwargs):
        id_zona=request.GET['id']

        print (id_zona)





        univer=universidad.objects.filter(zona__id=id_zona)
        print(univer)
        data= serializers.serialize('json',univer,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')



class BusquedaCampusView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_uni=request.GET['id']
        print (id_uni)

        facul=campus.objects.filter(universidad__id=id_uni)
        print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')






class BusquedaFacuView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_campus=request.GET['id']
        print (id_campus)

        facul=facultad.objects.filter(campus__id=id_campus)
        print(facul)
        data= serializers.serialize('json',facul,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')

class BusquedaCarreraView(TemplateView):
    def get(self,request,*args, **kwargs):
        id_facul=request.GET['id']
        print (id_facul)

        carrer=carrera.objects.filter(facultad__id=id_facul)
        print(carrer)
        data= serializers.serialize('json',carrer,
                            fields=('id','Nombre'))
        return HttpResponse(data, content_type='application/json')
