from django.db import models
from apps.catalogos.municipio.models import Municipio
from apps.catalogos.plaza.models import DetallePlaza
from apps.catalogos.profesion.models import Profesion

# Create your models here.
class Postulante(models.Model):
    ID_Postulante = models.AutoField(primary_key=True)
    Cedula = models.CharField(verbose_name="Cédula", max_length=24, unique=True)
    Nombre_Postulante = models.CharField(verbose_name="Nombre del Postulante", max_length=56)
    Apellidos = models.CharField(verbose_name="Apellidos", max_length=56)
    Sexo = models.CharField(verbose_name="Sexo", max_length=17)
    Correo = models.CharField(verbose_name="Correo Electrónico", max_length=100)
    Telefono = models.CharField(verbose_name="Teléfono", max_length=16)
    Fecha_Nacimiento = models.CharField(verbose_name="Fecha Nacimiento", max_length=24)
    Direccion = models.CharField(verbose_name="Dirección", max_length=100)
    Experiencia_Laboral = models.CharField(verbose_name="Experiencia Laboral", max_length=100)
    ID_Municipio = models.ForeignKey(Municipio, verbose_name="Municipio", on_delete=models.PROTECT)
    ID_Profesion = models.ForeignKey(Profesion, verbose_name="Profesión", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Postulantes"

    def __str__(self):
        return f"{self.Nombre_Postulante} {self.Apellidos}"


class DetallePostulante(models.Model):
    ID_DETALLE_POSTULANTE = models.AutoField(primary_key=True)
    ID_DetallePlaza = models.ForeignKey(DetallePlaza, verbose_name="DetallePlaza", on_delete=models.PROTECT)
    ID_Postulante = models.ForeignKey(Postulante,related_name='detalles', verbose_name="Postulante", on_delete=models.PROTECT)
    Comentarios = models.CharField(verbose_name="Comentarios", max_length=200)

    class Meta:
        verbose_name_plural = "Detalles de Postulante"

    def __str__(self):
        return f"{self.ID_Postulante} {self.Comentarios}"

