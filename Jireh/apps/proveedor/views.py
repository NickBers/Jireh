from django.shortcuts import render,redirect
from .models import Proveedor
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from .form import ProveedorForm
from django.urls import reverse_lazy  
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
"""def proveedor(request):
    proveedor = Proveedor.objects.all()
    return render(request,"administrador/proveedor.html",{'proveedor': proveedor})"""



class ProveedorListView(LoginRequiredMixin,ListView):
    model=Proveedor
    template_name= 'administrador/proveedor/proveedor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Proveedor.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 
    
class CreateProveedorView(LoginRequiredMixin,CreateView):
    model=Proveedor
    form_class=ProveedorForm
    template_name='administrador/proveedor/create.html'
    success_url = reverse_lazy('ShowProveedor')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('CreateProveedor')
        context['list_url'] = reverse_lazy('ShowProveedor')
        context['action'] = 'add'
        return context  

class UpdateProveedorView(LoginRequiredMixin,UpdateView):
    model=Proveedor
    form_class=ProveedorForm
    template_name='administrador/proveedor/create.html'
    success_url = reverse_lazy('ShowProveedor')


    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opci??n'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('CreateProveedor')
        context['list_url'] = reverse_lazy('ShowProveedor')
        context['action'] = 'edit'
        return context  

class DeleteProveedorview(LoginRequiredMixin,DeleteView):
    model = Proveedor
    template_name = 'administrador/proveedor/delete.html'
    success_url = reverse_lazy('ShowProveedor')
 
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            self.object.delete()
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('CreateProveedor')
        context['list_url'] = reverse_lazy('ShowProveedor')
        context['action'] = 'edit'
        return context  




    
