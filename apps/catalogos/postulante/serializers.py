from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from .models import Postulante, DetallePostulante

class DetallePostulanteSerializer(ModelSerializer):
    Detalle_Plaza = CharField(source='ID_DetallePlaza.Descripcion', read_only=True)
    class Meta:
        model = DetallePostulante
        fields = ['ID_DetallePlaza', 'Detalle_Plaza','Comentarios']

class PostulanteSerializer(ModelSerializer):
    Nombre_Municipio = CharField(source='ID_Municipio.Nombre', read_only=True)
    Nombre_Profesion = CharField(source='ID_Profesion.Nombre_Profesion', read_only=True)
    detalles = DetallePostulanteSerializer(many=True)
    class Meta:
        model = Postulante
        fields = ['Cedula', 'Nombre_Postulante', 'Apellidos', 'Sexo', 'Correo', 'Telefono', 'Fecha_Nacimiento',
                  'Direccion', 'Experiencia_Laboral', 'ID_Municipio', 'Nombre_Municipio', 'ID_Profesion', 'Nombre_Profesion', 'detalles']