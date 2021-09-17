from django.db import models
from apps.producto.models import Producto
from apps.cliente.models import Clientes

class Detalles(models.Model):
    cantidad=models.IntegerField(null=False)
    monto=models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s ' % (self.id, self.producto)

class Venta(models.Model):

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    detalles=models.ManyToManyField(Detalles,verbose_name="Detalles")
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s' % (self.detalles, self.cliente)

    


    
