from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import *

class ProyectoListView(ListView):
    template_name="proyectos_list.html"
    model=Proyectos
    # def get_context_data(self, **kwargs):
    #     ctx = super(ProyectoListView, self).get_context_data(**kwargs)
    #     ctx['fields'] = [field.name for field in Proyectos._meta.get_fields()]
    #     return ctx

class EcorregionListView(ListView):
    template_name="lugares_list.html"
    model=Ecorregion

class RegistrosListView(ListView):
    template_name="registros_list.html"
    model=RegistroBioEspecies

