from django.forms import *
from .models import Venta
from datetime import datetime


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%'
            }),
            'created': DateInput(
                format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                    'autocomplete': 'off',
                    'class': 'form-control datetimepicker-input',
                    'id': 'created',
                    'data-target': '#created',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'iva': NumberInput(attrs={
                'class': 'form-control'
            }),
            'subtotal': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }
