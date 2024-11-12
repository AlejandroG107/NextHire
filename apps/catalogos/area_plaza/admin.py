from django.contrib import admin
from apps.catalogos.area_plaza.models import AreaPlaza

# Register your models here.
@admin.register(AreaPlaza)
class AreaPlazaAdmin(admin.ModelAdmin):
    search_fields = ['Codigo', 'Descripcion']
    list_display = ['Codigo', 'Descripcion']

