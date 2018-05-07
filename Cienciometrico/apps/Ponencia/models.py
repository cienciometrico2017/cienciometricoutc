# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from apps.palabraClave.models import palabraClave
from apps.Articulos_Cientificos.models import articulos_cientificos
from django.contrib.auth.models import User

class ponencia (models.Model):
  CHOICES = (
    ('Sí', 'Sí'),
    ('No', 'No'),
  )
  nombrePonencia = models.CharField(max_length=150, null=False, blank=False)
  lugarPonencia = models.CharField(max_length=150, null=False, blank=False)
  tituloPonencia = models.CharField(max_length=70, null=False, blank=False)
  fechaPonencia = models.DateField(null=False, blank=False)
  anio = models.IntegerField(null=True, blank=True)
  nivelAutoria = models.CharField(max_length=100, null=True, blank=True)
  palabrasClave = models.ManyToManyField(palabraClave)
  resumen = models.TextField(null=True, blank=True)
  certificado = models.CharField(max_length=100, null=True, blank=True)
  urlPonencia = models.URLField(null=True, blank=True)
  financiamiento = models.CharField(max_length=2, null=True, blank=True,choices=CHOICES)
  informe = models.FileField(upload_to='informes/', null=True, blank=True)
  articuloCientifico = models.ManyToManyField(articulos_cientificos)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  def __str__(self): return '{}'.format(self.nombrePonencia)



