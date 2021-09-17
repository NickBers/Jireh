from django.db import models

class Marca(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)

    class Meta:
            verbose_name='Marca'
            verbose_name_plural='Marcas'

    def __str__(self):
        return self.nombre
