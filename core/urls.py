from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipo/', include('apps.equipos.urls')), 
    path('', include('apps.inicio.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', include('apps.login.urls')), 
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)