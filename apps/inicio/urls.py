# inventario/urls.py
from django.urls import path
from . import views

app_name = 'inicio'  # Define el espacio de nombres aquí

urlpatterns = [
    
  path('', views.home, name='inicioHome')

]