"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from registro.views import *

urlpatterns = [
    path("List_proyectos",ProyectoListView.as_view(), name="Lista de proyectos"),
    path("List_ecorregiones",EcorregionListView.as_view(), name="Lista de Ecorregiones"),
    path("List_registros",RegistrosListView.as_view(), name="Lista de Registros"),
    path("descarga_registros",RegistrosListView.as_view()),
   
    path('admin/', admin.site.urls),
]
