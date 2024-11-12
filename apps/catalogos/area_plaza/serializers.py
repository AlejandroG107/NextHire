from rest_framework.serializers import  ModelSerializer

from .models import AreaPlaza

class AreaPlazaSerializer(ModelSerializer):
    class Meta:
        model = AreaPlaza
        fields = ['Codigo', 'Descripcion']