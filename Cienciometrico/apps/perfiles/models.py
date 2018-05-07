from django.db import models
from django.contrib.auth.models import User
from apps.roles.models import Rol
# Create your models here.
class Perfil(models.Model):
    CHOICES = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )
    cedula = models.CharField(max_length=10, blank=True)
    photo = models.ImageField(upload_to='foto/', null=True,blank=True)
    direccion = models.CharField(max_length=500, blank=True)
    coordenadas = models.CharField(max_length=450, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    genero = models.CharField(max_length=100, blank=True, choices=CHOICES)
    nacionalidad = models.CharField(max_length=100, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    roles = models.ManyToManyField(Rol)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return '{}  {}'.format(self.cedula, self.direccion)

    # Permisos

    class Meta:
        permissions = (
            ("ver_perfil", "ver perfil"),
        )