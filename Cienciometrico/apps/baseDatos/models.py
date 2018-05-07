from django.db import models
from django.contrib.auth.models import User
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion
from apps.Investigador.models import investigador
from apps.Ambito_Investigativo.models import ambito_investigativo
# Create your models here.
class baseDatos(models.Model):
 BaseDatos=models.CharField(max_length=200)
 Url = models.URLField(null=True, blank=True)
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 def __str__(self): return '{}'.format(self.BaseDatos)