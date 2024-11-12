from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.tipo_empresa.models import TipoEmpresa
from .serializers import TipoEmpresaSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin

# Create your views here.
class TipoEmpresaAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: TipoEmpresaSerializer(many=True)})
    def get(self, request):
        tipoempresa = TipoEmpresa.objects.all().order_by('ID_TipoEmpresa')
        page = self.paginate_queryset(tipoempresa, request)

        if page is not None:
            serializer = TipoEmpresaSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        tipoempresa = TipoEmpresa.objects.all()
        serializer = TipoEmpresaSerializer(tipoempresa, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoEmpresaSerializer, responses={201: TipoEmpresaSerializer})
    def post(self, request):

        serializer = TipoEmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoEmpresaDetails(APIView):

    @swagger_auto_schema(responses={200: TipoEmpresaSerializer})
    def get(self, request, pk):

        try:
            tipoempresa = TipoEmpresa.objects.get(pk=pk)
        except TipoEmpresa.DoesNotExist:
            return Response({'error': 'Tipo de empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TipoEmpresaSerializer(tipoempresa)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TipoEmpresaSerializer, responses={200: TipoEmpresaSerializer})
    def put(self, request, pk):

        try:
            tipoempresa = TipoEmpresa.objects.get(pk=pk)
        except TipoEmpresa.DoesNotExist:
            return Response({'error': 'Tipo de empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoEmpresaSerializer(tipoempresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=TipoEmpresaSerializer, responses={200: TipoEmpresaSerializer})
    def patch(self, request, pk):

        try:
            tipoempresa = TipoEmpresa.objects.get(pk=pk)
        except TipoEmpresa.DoesNotExist:
            return Response({'error': 'Tipo de empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TipoEmpresaSerializer(tipoempresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            tipoempresa = TipoEmpresa.objects.get(pk=pk)
        except TipoEmpresa.DoesNotExist:
            return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        tipoempresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)