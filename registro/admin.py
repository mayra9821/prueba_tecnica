from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import RegistroBioEspecies,Proyectos,Ecorregion


class RegistroBioEspeciesAdmin(admin.ModelAdmin):
    list_display = ('identificador','especie','familia','nombre_comun','proyecto','base_registro','anio_identificacion','departamento','municipio','localidad','latitud','longitud','autor','fecha_captura','ecorregion')
    
admin.site.register(RegistroBioEspecies,RegistroBioEspeciesAdmin)

class ProyectosAdmin(admin.ModelAdmin):
    list_display = ('idproyecto','nombre')
admin.site.register(Proyectos,ProyectosAdmin)

class EcorregionAdmin(admin.ModelAdmin):
    list_display = ('idecorregion','nombre')
admin.site.register(Ecorregion,EcorregionAdmin)



    