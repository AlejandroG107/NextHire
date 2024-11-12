from django.db import models

class Departamento(models.Model):
    ID_Departamento = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código', max_length=50, unique=True)
    Nombre = models.CharField(verbose_name='Nombre', max_length=100)
    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f"{self.Codigo} - {self.Nombre}"

