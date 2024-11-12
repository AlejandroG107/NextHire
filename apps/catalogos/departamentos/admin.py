from django.contrib import admin
from apps.catalogos.departamentos.models import Departamento

# Register your models here.
@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ('Codigo', 'Nombre')
    list_display = ('Codigo', 'Nombre')