# inventario/urls.py
from django.urls import path
from . import views

app_name = 'login'  # Define el espacio de nombres aquí

urlpatterns = [
    path('login_user', views.login_user, name="login_new"),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),
    path('login_error', views.error, name="loginError"),
]