from django.forms import *
from .models import Proveedor

class ProveedorForm(ModelForm):
    def __init__(self,*args,**kwards):
        super().__init__(*args,**kwards)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model= Proveedor
        fields= '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder':'Ingrese un apellido',
                }
            ),
            'empresa': TextInput(
                attrs={
                    'placeholder':'Ingrese nombre de la empresa',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder':'Ingrese un email',
                    'required':False
                }
            ),
            'numero': TextInput(
                attrs={
                    'placeholder':'Ingrese numero telefonico',
                    'required':False
                }
            ),
                
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
         
