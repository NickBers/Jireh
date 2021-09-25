from django.db import models

class Automovil(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    modelo = models.CharField('modelo', max_length=150, blank=False, null=False)
    pais = models.CharField('Pais', max_length=150, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
            verbose_name='Automovil'
            verbose_name_plural='Automovils'
            ordering = ["-created"]

    def __str__(self):
        return self.nombre

