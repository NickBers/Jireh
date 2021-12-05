from django.urls import path
from .views import *


urlpatterns = [
    path('',ProveedorListView.as_view(), name="ShowProveedor"),
    path('proveedor/create/',CreateProveedorView.as_view(), name="CreateProveedor"),
    path('proveedor/update/<int:pk>/', UpdateProveedorView.as_view(), name="UpdateProveedor"),
    path('proveedor/delete/<int:pk>/', DeleteProveedorview.as_view(), name="DeleteProveedor")
    
]