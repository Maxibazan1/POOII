from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class Persona(models.Model):
    apellido = models.CharField(max_length=30)
    nombre = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, verbose_name='D.N.I')
    email = models.EmailField(max_length=200, unique=True, null=False)
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento')
    vive = models.BooleanField(default=True);
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    legajo = RichTextField(default='legajo')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

class Contacto(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField(max_length=250)
    mensaje = models.TextField(max_length=300)
        
