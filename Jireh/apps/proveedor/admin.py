from django.contrib import admin

from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Proveedor)

