from django.contrib import admin
from apps.catalogos.empresa.models import Empresa

# Register your models here.
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Nombre_Empresa']
    list_display = ['Codigo', 'Nombre_Empresa', 'Direccion', 'Telefono', 'Correo', 'ID_Municipio', 'ID_TipoEmpresa']
