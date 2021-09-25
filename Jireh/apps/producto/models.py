from django.db import models

from apps.proveedor.models import Proveedor
from apps.categoria.models import Categoria
from apps.automovil.models import Automovil
from apps.marca.models import Marca

class Producto(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    codigo=models.CharField(max_length=200, verbose_name="Codigo")
    imagen=models.ImageField(upload_to='media',verbose_name='Imagen', null=True)
    pvp=models.IntegerField(verbose_name="Precio venta publico")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    automovil=models.ForeignKey(Automovil,on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
            verbose_name='Producto'
            verbose_name_plural='Productos'
            ordering = ["-created"]

    def __str__(self):
        return self.nombre