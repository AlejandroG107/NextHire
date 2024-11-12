from django.db import models
from apps.catalogos.municipio.models import Municipio
from apps.catalogos.tipo_empresa.models import TipoEmpresa

# Create your models here.
class Empresa(models.Model):
    ID_Empresa = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name="Código", max_length=50, unique=True)
    Nombre_Empresa = models.CharField(verbose_name="Nombre Empresa", max_length=100)
    Direccion = models.CharField(verbose_name="Dirección", max_length=200)
    Telefono = models.CharField(verbose_name='Teléfono', max_length=16)
    Correo = models.CharField(verbose_name="Correo Electrónico", max_length=100)
    ID_Municipio = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.PROTECT)
    ID_TipoEmpresa = models.ForeignKey(TipoEmpresa, verbose_name="Tipo Empresa", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f"{self.Codigo} {self.Nombre_Empresa}"
