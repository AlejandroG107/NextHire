from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.departamentos.models import Departamento
from .serializers import DepartamentoSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin
# Create your views here.

class DepartamentoAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: DepartamentoSerializer(many=True)})
    def get(self, request):
        departamento = Departamento.objects.all().order_by('ID_Departamento')
        page = self.paginate_queryset(departamento, request)

        if page is not None:
            serializer = DepartamentoSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={201: DepartamentoSerializer})
    def post(self, request):

        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetails(APIView):

    @swagger_auto_schema(responses={200: DepartamentoSerializer})
    def get(self, request, pk):

        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def put(self, request, pk):

        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=DepartamentoSerializer, responses={200: DepartamentoSerializer})
    def patch(self, request, pk):

        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializer(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)