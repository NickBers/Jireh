from django.db import models

from apps.proveedor.models import Proveedor
from apps.categoria.models import Categoria
from apps.automovil.models import Automovil
from apps.marca.models import Marca
from Jireh.settings import MEDIA_URL, STATIC_URL
from datetime import datetime
from django.forms import model_to_dict
import select2.fields
import select2.models


class Producto(models.Model):
    nombre=models.CharField(max_length=200, verbose_name="Nombre")
    codigo=models.CharField(max_length=200, verbose_name="Codigo")
    imagen=models.ImageField(upload_to='media',verbose_name='Imagen',blank=True, null=True)
    pvp=models.IntegerField(verbose_name="Precio venta publico")
    proveedor=select2.fields.ForeignKey(Proveedor,on_delete=models.CASCADE,overlay="Selecciona un provedor...")
    categoria=select2.fields.ForeignKey(Categoria,on_delete=models.CASCADE, overlay="Selecciona una categoria...")
    automovil=select2.fields.ForeignKey(Automovil,on_delete=models.CASCADE,overlay="Seleccione automovil...")
    marca=select2.fields.ForeignKey(Marca,on_delete=models.CASCADE,overlay="Selecciona la marca...")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    
    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()
        item['imagen'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
            verbose_name='Producto'
            verbose_name_plural='Productos'
            ordering = ["-created"]

    