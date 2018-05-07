from django.db import models
from apps.palabraClave.models import palabraClave
from apps.Linea_Investigacion.models import linea_investigacion
from apps.Sub_Lin_Investigacion.models import sub_lin_investigacion


from django.contrib.auth.models import User
# Create your models here.
class proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    financiamiento = models.CharField(max_length=2)
    montoFinanciado = models.CharField(max_length=200)
    montorecibido = models.CharField(max_length=200)
    integrantes = models.ForeignKey(User);
    resumen=models.TextField()
    palabrasClaves = models.ManyToManyField(palabraClave)
    lineaInvestigacion = models.ForeignKey(linea_investigacion)
    subLinea= models.ForeignKey(sub_lin_investigacion)
    tipo = models.CharField(max_length=255)
    documentos = models.FileField(upload_to='proyecto/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ("ver_Proyectos", "ver Proyectos"),
        )