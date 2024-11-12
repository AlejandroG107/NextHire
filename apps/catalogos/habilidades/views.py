from shutil import posix

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HabilidadesSerializer, DetalleHabilidadesSerializer
from .models import Habilidades, DetalleHabilidades, Postulante
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction

class HabilidadesAPIView(APIView):
    @swagger_auto_schema(responses={200: HabilidadesSerializer()})
    def get(self, request, pk=None):
        habilidades = Habilidades.objects.all()
        serializer = HabilidadesSerializer(habilidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=HabilidadesSerializer)
    def post(self, request):
        serializer = HabilidadesSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    habilidad = Habilidades.objects.create(
                        Codigo=serializer.validated_data['Codigo'],
                        Nombre_Habilidad=serializer.validated_data['Nombre_Habilidad'],
                    )
                    for detalle_data in serializer.validated_data['detalles']:
                        descripcion = detalle_data['Descripcion']
                        postulante = get_object_or_404(Postulante,
                                                       pk=detalle_data['ID_Postulante'].ID_Postulante)
                        DetalleHabilidades.objects.create(
                            Id_Habilidades=habilidad,
                            Descripcion=descripcion,
                            ID_Postulante = postulante
                        )
                habilidad_serializer = HabilidadesSerializer(habilidad)
                return Response(habilidad_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Devuelve un error en caso de excepción
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleHabilidadDetails(APIView):

    @swagger_auto_schema(responses={200: HabilidadesSerializer()})
    def get(self, request, pk):
        habilidad = get_object_or_404(Habilidades, pk=pk)
        serializer = HabilidadesSerializer(habilidad)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        habilidad = get_object_or_404(Habilidades, pk=pk)
        try:
            with transaction.atomic():
                DetalleHabilidades.objects.filter(Id_Habilidades=habilidad).delete()
                habilidad.delete()
            return Response({"message": "Habilidad eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)