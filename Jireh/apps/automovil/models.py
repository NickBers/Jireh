from django.db import models

class Automovil(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    modelo = models.CharField('modelo', max_length=150, blank=False, null=False)
    pais = models.CharField('Pais', max_length=150, blank=False, null=False)

    class Meta:
            verbose_name='Automovil'
            verbose_name_plural='Automovils'

    def __str__(self):
        return self.nombre

