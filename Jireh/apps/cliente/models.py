from django.db import models

class Clientes(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=150, blank=False, null=False)
    
    class Meta:
            verbose_name='Cliente'
            verbose_name_plural='Clientes'

    def __str__(self):
        return self.nombre
