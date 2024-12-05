"""
URL configuration for VentaAutos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestion.views import busqueda_autos, buscar, contacto, crud, insertar_auto
#Importa las vistas de la aplicación Gestion que se asociarán con las rutas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_autos/', busqueda_autos, name='busqueda_autos'),
    path('buscar/', buscar),
    path('contacto/', contacto, name='contacto'),
    path('consultar/', crud, name='crud'),
    path('insertar_auto/', insertar_auto, name='insertar_auto'), 
]

