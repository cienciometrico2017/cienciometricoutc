# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from apps.Investigador.models import investigador

class grado_competencia(models.Model):
    Valor = models.IntegerField()
    investigador=models.ForeignKey(investigador,null=True,blank=True ,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.Valor)
