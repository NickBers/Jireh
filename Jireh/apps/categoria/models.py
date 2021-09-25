from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)

    class Meta:
            verbose_name='Categoria'
            verbose_name_plural='Categorias'
            ordering = ["-id"]

    def __str__(self):
        return self.nombre


