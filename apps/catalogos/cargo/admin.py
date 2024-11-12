from django.contrib import admin
from apps.catalogos.cargo.models import Cargo

# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    search_fields = ('Codigo', 'Nombre_cargo')
    list_display = ('Codigo', 'Nombre_cargo')
