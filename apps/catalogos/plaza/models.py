from django.db import models
from apps.catalogos.empresa.models import Empresa
from apps.catalogos.cargo.models import Cargo
from apps.catalogos.area_plaza.models import AreaPlaza

# Create your models here.
class Plaza(models.Model):
    ID_Plaza = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name="Código Plaza", max_length=16)
    Salario = models.FloatField(verbose_name="Salario")
    Descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    ID_Empresa = models.ForeignKey(Empresa, verbose_name="Empresa", on_delete=models.PROTECT)
    ID_Cargo = models.ForeignKey(Cargo, verbose_name="Cargo", on_delete=models.PROTECT)
    ID_AreaPLAZA = models.ForeignKey(AreaPlaza, verbose_name="AreaPlaza", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Plazas"

    def __str__(self):
        return f"{self.Descripcion} {self.Salario}"

class DetallePlaza(models.Model):
    ID_DetallePlaza = models.AutoField(primary_key=True)
    Id_Plaza = models.ForeignKey(Plaza, related_name='detalles', verbose_name="Plaza", on_delete=models.PROTECT)
    Descripcion = models.CharField(verbose_name="Descripcion", max_length=300)
    class Meta:
        verbose_name_plural = "Detalles de Plazas"

    def __str__(self):
        return f"{self.ID_DetallePlaza} - {self.Id_Plaza} - {self.Descripcion}"






