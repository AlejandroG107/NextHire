from rest_framework.serializers import  ModelSerializer

from .models import Municipio

class MunicipioSerializer(ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['Departamento', 'Codigo', 'Nombre']