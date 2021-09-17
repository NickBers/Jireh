from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=150, blank=False, null=False)
    empresa = models.CharField('Empresa', max_length=150, blank=False, null=False)
    email = models.CharField('Email', max_length=150, blank=False, null=True)
    numero = models.CharField('Numero Telefonico', max_length=150, blank=False, null=True)
    


    class Meta:
            verbose_name='Proveedor'
            verbose_name_plural='Proveedor'

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)