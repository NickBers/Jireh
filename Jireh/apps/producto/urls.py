from django.urls import path
from .views import *



urlpatterns = [
    path('',ProductoListView.as_view(), name="ShowProducto"), 
    path('producto/create/',ProductoCreateView.as_view(), name="CreateProducto") 
]