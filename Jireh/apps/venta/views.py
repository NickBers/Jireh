from django.shortcuts import render,redirect
from .models import Venta, Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy  
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import SaleForm

class saleCreateView(LoginRequiredMixin,CreateView):
    model=Venta
    template_name= 'administrador/ventas/create.html'
    form_class = SaleForm
    reverse_lazy = reverse_lazy('index')
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data=[]
                prods = Producto.objects.filter(codigo__contains=request.POST['term'])[0:10]
                for i in prods:
                    item=i.toJSON() 
                    item['value']=i.nombre
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data,safe=False) 

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Creacion de una venta'
            context['entity'] = 'Venta'
            context['action'] = 'add'
            return context  
# Create your views here.
