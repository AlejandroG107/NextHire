from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.empresa.models import Empresa
from .serializers import EmpresaSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin
# Create your views here.

class EmpresaAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: EmpresaSerializer(many=True)})
    def get(self, request):

        empresa = Empresa.objects.all().order_by('ID_Empresa')
        page = self.paginate_queryset(empresa, request)

        if page is not None:
            serializer = EmpresaSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        empresa = Empresa.objects.all()
        serializer = EmpresaSerializer(empresa, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EmpresaSerializer, responses={201: EmpresaSerializer})
    def post(self, request):

        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpresaDetails(APIView):

    @swagger_auto_schema(responses={200: EmpresaSerializer})
    def get(self, request, pk):

        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EmpresaSerializer, responses={200: EmpresaSerializer})
    def put(self, request, pk):

        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=EmpresaSerializer, responses={200: EmpresaSerializer})
    def patch(self, request, pk):

        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmpresaSerializer(empresa, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
