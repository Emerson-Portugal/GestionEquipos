from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Create your views here.


app_name = 'login'

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('equipos:inicio')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return redirect('/')	
						


	else:
		return render(request, 'registration/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('equipos:inicio')


def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect('equipos:inicio')
	else:
		form = RegisterUserForm()

	return render(request, 'registration/register.html', {
		'form':form,
		})


# Error 

def error(request):
    return render(request, 'error.html')