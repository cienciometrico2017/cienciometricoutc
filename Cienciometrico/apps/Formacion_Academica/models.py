# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from apps.Investigador.models import investigador
class formacion_academica(models.Model):
 Nivel_Estudios=models.CharField(max_length=25,null=True)
 NombreTitulo=models.CharField(max_length=500,null=True)
 Fecha_Fin_Estudios=models.DateField(null=True)
 Nombre_Centro_Estudios=models.CharField(max_length=250,null=True)
 user = models.ForeignKey(User, on_delete=models.CASCADE)

 class Meta:
  permissions = (
   ("ver_formacionAcademica", "ver formacionAcademica"),
  )