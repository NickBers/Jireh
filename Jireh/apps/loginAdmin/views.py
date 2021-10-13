from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import *
from django.views.generic import FormView, RedirectView

class LoginView(LoginView):
    template_name='administrador/login/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('ShowProveedor')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LogoutRedirectView(RedirectView):
    pattern_name = 'login'
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
    
