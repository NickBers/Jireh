from django.db import models
from django.db import models
from datetime import datetime

from django.forms import model_to_dict

class Proveedor(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)
    apellido = models.CharField('Apellido', max_length=150, blank=False, null=False)
    empresa = models.CharField('Empresa', max_length=150, blank=False, null=False)
    email = models.CharField('Email', max_length=150, blank=False, null=True)
    numero = models.CharField('Numero Telefonico', max_length=150, blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
            verbose_name='Proveedor'
            verbose_name_plural='Proveedor'
            ordering = ["-created"]
            

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)