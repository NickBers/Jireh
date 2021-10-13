from django.urls import path, include
from apps.loginAdmin.views import *


urlpatterns = [
    path('', LoginView.as_view(),name='login'),
    path('logout/', LogoutRedirectView.as_view(),name='logout')
]