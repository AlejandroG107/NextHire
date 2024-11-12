from django.contrib import admin
from apps.catalogos.municipio.models import Municipio

# Register your models here.
@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ('Codigo', 'Nombre')
    list_display = ('Codigo', 'Nombre', 'Departamento')

