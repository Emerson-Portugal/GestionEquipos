# inventario/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'equipos'  # Define el espacio de nombres aquí

urlpatterns = [
    
  path('inicio/', views.home, name='inicio'), 

  # Agregar Equipos 

  path('equipos/', views.equipo_list, name='equipo_list'),
  path('equipos/create/<str:equipo_tipo>/', views.equipo_create, name='equipo_create'),
  path('equipos/update/<str:equipo_tipo>/<int:pk>/', views.equipo_update, name='equipo_update'),
  path('equipos/delete/<str:equipo_tipo>/<int:pk>/', views.equipo_delete, name='equipo_delete'),





  # Agregar Personas

  path('personas/', views.persona_list, name='persona_list'),
  path('personas/create/', views.persona_create, name='persona_create'),
  path('personas/<str:dni>/edit/', views.persona_update, name='persona_update'),
  path('personas/<str:dni>/delete/', views.persona_delete, name='persona_delete'),
  path('personas/<str:dni>/', views.persona_detail, name='persona_detail'),

]