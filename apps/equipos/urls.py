# inventario/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'equipos'  # Define el espacio de nombres aquí

urlpatterns = [
    
  path('inicio', views.home, name='inicio'), 

]