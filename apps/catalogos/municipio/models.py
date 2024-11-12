from django.db import models
from apps.catalogos.departamentos.models import Departamento


class Municipio(models.Model):
    Codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    Nombre = models.CharField(verbose_name='Nombre', max_length=100)
    Departamento = models.ForeignKey(Departamento, verbose_name='Departamento', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f"{self.Codigo} - {self.Nombre}"
