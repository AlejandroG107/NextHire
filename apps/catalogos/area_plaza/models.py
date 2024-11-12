from django.db import models
from apps.catalogos.cargo.models import Cargo

# Create your models here.
class AreaPlaza(models.Model):
    ID_AreaPLAZA = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código', max_length=16, unique=True)
    Descripcion = models.CharField(verbose_name='Descripcion', max_length=500)

    class Meta:
        verbose_name_plural = 'Areas de Plazas'

    def __str__(self):
        return f"{self.Codigo} - {self.Descripcion}"
