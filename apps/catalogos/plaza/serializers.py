from rest_framework.serializers import ModelSerializer, CharField
from .models import Plaza, DetallePlaza

class DetallePlazaSerializer(ModelSerializer):
    class Meta:
        model = DetallePlaza
        fields = ['Descripcion']

class PlazaSerializer(ModelSerializer):
    Nombre_Empresa = CharField(source='ID_Empresa.Nombre_Empresa', read_only=True)
    Nombre_Cargo = CharField(source='ID_Cargo.Nombre_cargo', read_only=True)
    Nombre_AreaPlaza = CharField(source='ID_AreaPLAZA.Descripcion', read_only=True)
    detalles = DetallePlazaSerializer(many=True)
    class Meta:
        model = Plaza
        fields = ['Codigo', 'Salario', 'Descripcion','ID_Empresa', 'Nombre_Empresa', 'ID_Cargo', 'Nombre_Cargo',
                  'ID_AreaPLAZA', 'Nombre_AreaPlaza', 'detalles']