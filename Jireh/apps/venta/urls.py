from django.urls import path
from .views import *


urlpatterns = [
    path('ventas/create/',saleCreateView.as_view(), name="CreateVenta"),
  
]