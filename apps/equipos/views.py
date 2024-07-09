from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
import json
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse
from functools import wraps
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



# Create your views here.


app_name = 'equipos'


## Decoradores


def plural_to_singular(plural):
    # Diccionario de palabras
    plural_singular = {
        "administrativo": "administrativo",
        "almacen": "almacen",
        "supervisor": "supervisor",
        "trabajador": "trabajador",
    }

    return plural_singular.get(plural, "error")

# OBTENER COLOR Y GRUPO DE UN USUARIO
def get_group_and_color(user):
    group = user.groups.first()
    group_id = None
    group_name = None
    group_name_singular = None
    color = None

    if group:
        if group.name == 'administrativo':
            color = 'bg-primary'
        elif group.name == 'supervisor':
            color = 'bg-secondary'
        elif group.name == 'trabajador':
            color = 'bg-danger'

        group_id = group.id
        group_name = group.name
        group_name_singular = plural_to_singular(group.name)

    return group_id, group_name, group_name_singular, color

# DECORADOR PERSONALIZADO PARA VISTAS BASADAS EN FUNCIÓN
def add_group_name_to_context(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        group_id, group_name, group_name_singular, color = get_group_and_color(user)

        # Agregar contexto adicional al request
        extra_context = {
            'group_name': group_name,
            'group_name_singular': group_name_singular,
            'color': color
        }

        # Pasar el extra_context al render dentro de la vista
        response = view_func(request, extra_context=extra_context, *args, **kwargs)
        return response

    return _wrapped_view

# Home 
@add_group_name_to_context
def home(request, extra_context):
    return render(request, 'home.html', extra_context)