from django.shortcuts import render

# Create your views here.
app_name = 'inicio'


# Home 

def home (request):
    return render(request, 'baseInicio.html')