from django.contrib import admin
from apps.catalogos.habilidades.models import Habilidades, DetalleHabilidades


# Register your models here.
@admin.register(Habilidades)
class HabilidadesAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Nombre_Habilidad']
    list_display = ['Codigo', 'Nombre_Habilidad']

@admin.register(DetalleHabilidades)
class DetalleHabilidadesAdmin(admin.ModelAdmin):
    search_fields = ['ID_Postulante', 'ID_DetalleHabilidades', 'Id_Habilidades']
    list_display = ['ID_DetalleHabilidades', 'ID_Postulante', 'Id_Habilidades']

