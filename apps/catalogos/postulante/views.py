from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostulanteSerializer, DetallePostulanteSerializer
from .models import Postulante, DetallePostulante, Municipio, Profesion
from drf_yasg.utils import swagger_auto_schema
from django.db import transaction

from ..plaza.models import DetallePlaza


class PostulanteAPIView(APIView):
    @swagger_auto_schema(responses={200: PostulanteSerializer()})
    def get(self, request, pk=None):
        postulantes = Postulante.objects.all()
        serializer = PostulanteSerializer(postulantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PostulanteSerializer)
    def post(self, request):
        serializer = PostulanteSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    municipio = get_object_or_404(Municipio, pk=serializer.validated_data['ID_Municipio'].id)
                    profesion = get_object_or_404(Profesion, pk=serializer.validated_data['ID_Profesion'].ID_Profesion)
                    postulante = Postulante.objects.create(
                        Cedula=serializer.validated_data['Cedula'],
                        Nombre_Postulante=serializer.validated_data['Nombre_Postulante'],
                        Apellidos=serializer.validated_data['Apellidos'],
                        Sexo=serializer.validated_data['Sexo'],
                        Correo=serializer.validated_data['Correo'],
                        Telefono=serializer.validated_data['Telefono'],
                        Fecha_Nacimiento=serializer.validated_data['Fecha_Nacimiento'],
                        Direccion=serializer.validated_data['Direccion'],
                        Experiencia_Laboral=serializer.validated_data['Experiencia_Laboral'],
                        ID_Municipio=municipio,
                        ID_Profesion=profesion
                    )
                    for detalle_data in serializer.validated_data['detalles']:
                        comentarios = detalle_data['Comentarios']
                        detalleplaza = get_object_or_404(DetallePlaza,
                                                       pk=detalle_data['ID_DetallePlaza'].ID_DetallePlaza)
                        DetallePostulante.objects.create(
                            ID_Postulante=postulante,
                            ID_DetallePlaza=detalleplaza,
                            Comentarios=comentarios
                        )

                postulante_serializer = PostulanteSerializer(postulante)
                return Response(postulante_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                # Devuelve un error en caso de excepción
                return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetallePostulanteDetails(APIView):

    @swagger_auto_schema(responses={200: PostulanteSerializer()})
    def get(self, request, pk):
        postulante = get_object_or_404(Postulante, pk=pk)
        serializer = PostulanteSerializer(postulante)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        postulante = get_object_or_404(Postulante, pk=pk)
        try:
            with transaction.atomic():
                DetallePostulante.objects.filter(ID_Postulante=postulante).delete()
                postulante.delete()

            return Response({"message": "Postulante eliminado con éxito."}, status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)