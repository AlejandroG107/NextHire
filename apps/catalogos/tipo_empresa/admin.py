from django.contrib import admin
from apps.catalogos.tipo_empresa.models import TipoEmpresa

# Register your models here.
@admin.register(TipoEmpresa)
class TipoEmpresaAdmin(admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ['Nombre']