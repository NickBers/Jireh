from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=150, blank=False, null=False)


    def __str__(self):
        return self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
            verbose_name='Categoria'
            verbose_name_plural='Categorias'
            ordering = ["-id"]

 


