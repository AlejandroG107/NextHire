from django.db import models

# Create your models here.
class TipoEmpresa(models.Model):
    ID_TipoEmpresa = models.AutoField(primary_key=True)
    Nombre = models.CharField(verbose_name="Nombre", max_length=100)

    class Meta:
        verbose_name_plural = "Tipos de Empresas"

    def __str__(self):
        return f"{self.Nombre}"
