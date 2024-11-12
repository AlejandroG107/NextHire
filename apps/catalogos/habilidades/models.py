from django.db import models
from apps.catalogos.postulante.models import Postulante

# Create your models here.
class Habilidades(models.Model):
    ID_Habilidade = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código', max_length=20, unique=True)
    Nombre_Habilidad =models.CharField(verbose_name='Nombre Habilidad', max_length=100)

    class Meta:
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f'{self.Codigo} - {self.Nombre_Habilidad}'

class DetalleHabilidades(models.Model):
    ID_DetalleHabilidades = models.AutoField(primary_key=True)
    ID_Postulante = models.ForeignKey(Postulante, verbose_name="Postulante", on_delete=models.PROTECT)
    Id_Habilidades = models.ForeignKey(Habilidades,related_name='detalles', verbose_name='Habilidades', on_delete=models.PROTECT)
    Descripcion = models.CharField(verbose_name="Descripcion", max_length=300)

    class Meta:
        verbose_name_plural = 'Detalles de Habilidades'

    def __str__(self):
        return f"{self.ID_DetalleHabilidades} - {self.Descripcion}"