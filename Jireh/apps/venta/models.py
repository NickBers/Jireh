from django.db import models
from apps.producto.models import Producto
from apps.cliente.models import Clientes

class Venta(models.Model):

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s' % (self.total, self.cliente)

class Detalles(models.Model):
    cantidad=models.IntegerField(null=False)
    monto=models.FloatField(null=False)
    subtotal = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s ' % (self.id, self.producto)

    


    
