from django.shortcuts import render,redirect
import os
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"administrador/index.html")
