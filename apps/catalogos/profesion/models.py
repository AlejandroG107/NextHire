from django.db import models

# Create your models here.
class Profesion(models.Model):
    ID_Profesion = models.AutoField(primary_key=True)
    Codigo = models.CharField(verbose_name='Código' ,max_length=20, unique=True)
    Nombre_Profesion = models.CharField(verbose_name="Nombre Profesión", max_length=100)

    class Meta:
        verbose_name_plural = 'Profesiones'

    def __str__(self):
        return f'{self.Codigo}- {self.Nombre_Profesion}'
