# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.baseDatos.models import baseDatos
from apps.Revista.models import revista
from apps.palabraClave.models import palabraClave
from django.contrib.auth.models import User

# Create your models here.
class articulos_cientificos (models.Model):
    titulo=models.CharField(max_length=300,null=False, blank=False)
    anio = models.IntegerField(blank=False,null=False)
    estado = models.CharField(max_length=30,blank=False,null=False)
    iSSN = models.CharField(max_length=60,blank=False,null=False)
    url = models.URLField(max_length=300,blank=False,null=False)
    doi = models.URLField(max_length=300,blank=False,null=False)
    fechaPublicacion = models.DateField(blank=False,null=False)
    ciudad = models.CharField(max_length=150,blank=False,null=False)
    baseDatos = models.ForeignKey(baseDatos,blank=True,null=True)
    revista = models.ForeignKey(revista, null=True, blank=True, on_delete=models.CASCADE)
    volumen = models.CharField(max_length=150,blank=False,null=False)
    numero = models.CharField(max_length=150,blank=False,null=False)
    lineaInves = models.ForeignKey(linea_investigacion, max_length=150,blank=False,null=False)
    SubLinea = models.ForeignKey(sub_lin_investigacion, max_length=150,blank=False,null=False)
    resumen = models.TextField(max_length=150,blank=False,null=False)
    palabraClave = models.ForeignKey(palabraClave, max_length=150,blank=False,null=False)
    documento=models.FileField(blank=True,null=True)
    tipoArticulo = models.CharField(max_length=150,blank=False,null=False)
    gradoAutoria = models.CharField(max_length=150,blank=False,null=False)
    aprobado = models.CharField(max_length=150,blank=False,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ("ver_articulo", "ver articulo"),
        )
