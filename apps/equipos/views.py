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
from .models import Persona, Laptop, PC, Celular
from .forms import PersonaForm, LaptopForm, PCForm, CelularForm



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



# Agregar nuevos Equipos 

# CRUD Personas 


def persona_list(request):
    personas = Persona.objects.all()
    return render(request, 'persona_list.html', {'personas': personas})

def persona_detail(request, dni):
    persona = get_object_or_404(Persona, dni=dni)
    return render(request, 'persona_detail.html', {'persona': persona})

def persona_create(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos:persona_list')
    else:
        form = PersonaForm()
    return render(request, 'persona_form.html', {'form': form})

def persona_update(request, dni):
    persona = get_object_or_404(Persona, dni=dni)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            return redirect('equipos:persona_list')
    else:
        form = PersonaForm(instance=persona)
    return render(request, 'persona_form.html', {'form': form})

def persona_delete(request, dni):
    persona = get_object_or_404(Persona, dni=dni)
    if request.method == 'POST':
        persona.delete()
        return redirect('equipos:persona_list')
    return render(request, 'persona_confirm_delete.html', {'persona': persona})


# CRUD Equipos 


# Create
def equipo_create(request, equipo_tipo):
    if equipo_tipo == 'laptop':
        form_class = LaptopForm
    elif equipo_tipo == 'pc':
        form_class = PCForm
    elif equipo_tipo == 'celular':
        form_class = CelularForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos:equipo_list')
    else:
        form = form_class()
    
    return render(request, 'equipo_form.html', {'form': form, 'equipo_tipo': equipo_tipo})

# Read
def equipo_list(request):
    laptops = Laptop.objects.all()
    pcs = PC.objects.all()
    celulares = Celular.objects.all()
    return render(request, 'equipo_list.html', {'laptops': laptops, 'pcs': pcs, 'celulares': celulares})

# Update
def equipo_update(request, equipo_tipo, pk):
    if equipo_tipo == 'laptop':
        model = Laptop
        form_class = LaptopForm
    elif equipo_tipo == 'pc':
        model = PC
        form_class = PCForm
    elif equipo_tipo == 'celular':
        model = Celular
        form_class = CelularForm

    equipo = get_object_or_404(model, pk=pk)

    if request.method == 'POST':
        form = form_class(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipos:equipo_list')
    else:
        form = form_class(instance=equipo)

    return render(request, 'equipo_form.html', {'form': form, 'equipo_tipo': equipo_tipo})

# Delete
def equipo_delete(request, equipo_tipo, pk):
    if equipo_tipo == 'laptop':
        model = Laptop
    elif equipo_tipo == 'pc':
        model = PC
    elif equipo_tipo == 'celular':
        model = Celular

    equipo = get_object_or_404(model, pk=pk)
    
    if request.method == 'POST':
        equipo.delete()
        return redirect('equipos:equipo_list')
    
    return render(request, 'equipo_confirm_delete.html', {'equipo': equipo, 'equipo_tipo': equipo_tipo})

