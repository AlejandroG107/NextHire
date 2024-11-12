from rest_framework.serializers import ModelSerializer, CharField
from .models import Habilidades, DetalleHabilidades

class DetalleHabilidadesSerializer(ModelSerializer):
    Nombre_Postulantes = CharField(source='ID_Postulante.Nombre_Postulante', read_only=True)
    class Meta:
        model = DetalleHabilidades
        fields = ['ID_Postulante','Nombre_Postulantes','Descripcion']

class HabilidadesSerializer(ModelSerializer):
    detalles = DetalleHabilidadesSerializer(many=True)
    class Meta:
        model = Habilidades
        fields = ['Codigo', 'Nombre_Habilidad', 'detalles']