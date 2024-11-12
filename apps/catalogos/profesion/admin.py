from django.contrib import admin
from apps.catalogos.profesion.models import Profesion


# Register your models here.
@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Nombre_Profesion']
    list_display = ['Codigo', 'Nombre_Profesion']
