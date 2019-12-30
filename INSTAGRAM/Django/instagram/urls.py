from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')), # Esto es para que el aplicativo sea quien maneje las rutas desde un archivo llamado urls dentro de la carpeta de inicio.
]