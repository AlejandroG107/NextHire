from rest_framework.serializers import  ModelSerializer

from .models import Empresa

class EmpresaSerializer(ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['Codigo', 'Nombre_Empresa', 'Direccion', 'Telefono','Correo','ID_Municipio','ID_TipoEmpresa']