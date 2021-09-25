from django.db import models

class Clientes(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=150, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    class Meta:
            verbose_name='Cliente'
            verbose_name_plural='Clientes'
            ordering = ["-created"]

    def __str__(self):
        return self.nombre
