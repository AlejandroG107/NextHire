from idlelib.autocomplete import ID_CHARS

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize

from .serializers import PlazaSerializer, DetallePlazaSerializer
from .models import Plaza, DetallePlaza, Empresa, Cargo, AreaPlaza
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction

class PlazaAPIView(APIView):
    @swagger_auto_schema(responses={200: PlazaSerializer()})
    def get(self, request, pk=None):
        plaza = Plaza.objects.all()
        serializer = PlazaSerializer(plaza, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PlazaSerializer)
    def post(self, request):
        serializer = PlazaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    empresa = get_object_or_404(Empresa, pk=serializer.validated_data['ID_Empresa'].ID_Empresa)
                    cargo = get_object_or_404(Cargo, pk=serializer.validated_data['ID_Cargo'].ID_Cargo)
                    areaplaza = get_object_or_404(AreaPlaza, pk=serializer.validated_data['ID_AreaPLAZA'].ID_AreaPLAZA)
                    plaza = Plaza.objects.create(
                        Codigo=serializer.validated_data['Codigo'],
                        Salario = serializer.validated_data['Salario'],
                        Descripcion = serializer.validated_data['Descripcion'],
                        ID_Empresa=empresa,
                        ID_Cargo = cargo,
                        ID_AreaPLAZA = areaplaza
                    )
                    for detalle_data in serializer.validated_data['detalles']:
                        descripcion = detalle_data['Descripcion']

                        DetallePlaza.objects.create(
                            Id_Plaza=plaza,
                            Descripcion=descripcion,
                        )

                plaza_serializer = PlazaSerializer(plaza)
                return Response(plaza_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Devuelve un error en caso de excepción
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePlazaDetails(APIView):

    @swagger_auto_schema(responses={200: PlazaSerializer()})
    def get(self, request, pk):
        plaza = get_object_or_404(Plaza, pk=pk)
        serializer = PlazaSerializer(plaza)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        plaza = get_object_or_404(Plaza, pk=pk)

        try:
            with transaction.atomic():
                DetallePlaza.objects.filter(Id_Plaza=plaza).delete()
                plaza.delete()

            return Response({"message": "Plaza eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)