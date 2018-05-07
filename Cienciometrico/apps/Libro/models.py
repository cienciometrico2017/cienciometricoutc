from django.db import models
from django.contrib.auth.models import User
from apps.palabraClave.models import palabraClave
from apps.baseDatos.models import baseDatos
# Create your models here.

class libro(models.Model):
    Titulo=models.CharField(max_length=200, null=False, blank=False, error_messages={'required': 'Por favor, ingrese un titulo'})
    ISBN = models.CharField(max_length=100, null=True, blank=True)
    Anio = models.CharField(max_length=4, null=True, blank=True)
    Editorial = models.CharField(max_length=100, null=True, blank=True)
    Resumen=models.TextField(null=True)
    PalabrasClave = models.ForeignKey(palabraClave, on_delete=models.CASCADE)
    Documento = models.FileField(upload_to='libro/', null=True, blank=True)
    BaseDatos = models.ForeignKey(baseDatos, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    Url = models.URLField(null=True, blank=True)
    Doi = models.Doi = models.URLField(max_length=100, null=True, blank=True)
    UbicacionFisica = models.CharField(max_length=200, null=True, blank=True)
    capitulo = models.CharField(max_length=200, null=True, blank=True)
    gradoAutoria = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): return '{}'.format(self.Titulo)

    class Meta:
        permissions = (
            ("ver_libro", "ver libro"),
        )
