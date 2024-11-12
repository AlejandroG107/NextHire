from rest_framework.serializers import  ModelSerializer

from .models import Profesion

class ProfesionSerializer(ModelSerializer):
    class Meta:
        model = Profesion
        fields = 'ID_Profesion', 'Codigo', 'Nombre_Profesion'