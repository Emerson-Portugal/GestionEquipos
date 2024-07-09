from django import forms
from .models import Persona, Laptop, PC, Celular

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['dni', 'apellidos', 'nombres', 'cargo', 'area', 'correo', 'numero_celular']

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'

class PCForm(forms.ModelForm):
    class Meta:
        model = PC
        fields = '__all__'

class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = '__all__'