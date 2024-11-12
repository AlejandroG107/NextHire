from django.db import models

# Create your models here.
class Cargo (models.Model):
    ID_Cargo = models.AutoField(primary_key=True)
    Codigo = models.CharField(max_length=20, unique=True, verbose_name='Cargo')
    Nombre_cargo= models.CharField(max_length=100, verbose_name='Nombre Cargo')

    class Meta:
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return f'{self.Codigo} - {self.Nombre_cargo}'
