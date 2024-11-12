from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.municipio.models import Municipio
from .serializers import MunicipioSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin
# Create your views here.

class MunicipioAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: MunicipioSerializer(many=True)})
    def get(self, request):

        municipio = Municipio.objects.all().order_by('id')
        page = self.paginate_queryset(municipio, request)

        if page is not None:
            serializer = MunicipioSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        municipio = Municipio.objects.all()
        serializer = MunicipioSerializer(municipio, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={201: MunicipioSerializer})
    def post(self, request):

        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MunicipioDetails(APIView):

    @swagger_auto_schema(responses={200: MunicipioSerializer})
    def get(self, request, pk):

        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MunicipioSerializer(municipio)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def put(self, request, pk):

        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=MunicipioSerializer, responses={200: MunicipioSerializer})
    def patch(self, request, pk):

        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MunicipioSerializer(municipio, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            municipio = Municipio.objects.get(pk=pk)
        except Municipio.DoesNotExist:
            return Response({'error': 'Municipio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        municipio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)