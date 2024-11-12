from django.contrib import admin
from apps.catalogos.plaza.models import Plaza, DetallePlaza


# Register your models here.
@admin.register(Plaza)
class PlazaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Descripcion']
    list_display = ['Codigo', 'Salario', 'Descripcion', 'ID_Empresa', 'ID_Cargo', 'ID_AreaPLAZA']

@admin.register(DetallePlaza)
class DetallePlazaAdmin(admin.ModelAdmin):
    search_fields = ['Descripcion']
    list_display = ['ID_DetallePlaza', 'Id_Plaza', 'Descripcion']
