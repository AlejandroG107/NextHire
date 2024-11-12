from rest_framework.serializers import  ModelSerializer

from .models import TipoEmpresa

class TipoEmpresaSerializer(ModelSerializer):
    class Meta:
        model = TipoEmpresa
        fields = ['Nombre']