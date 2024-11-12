from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.area_plaza.models import AreaPlaza
from .serializers import AreaPlazaSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin

# Create your views here.
class ArePlazaAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: AreaPlazaSerializer(many=True)})
    def get(self, request):
        areplaza = AreaPlaza.objects.all().order_by('ID_AreaPLAZA')
        page = self.paginate_queryset(areplaza, request)

        if page is not None:
            serializer = AreaPlazaSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        areaplaza = AreaPlaza.objects.all()
        serializer = AreaPlazaSerializer(areaplaza, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AreaPlazaSerializer, responses={201: AreaPlazaSerializer})
    def post(self, request):

        serializer = AreaPlazaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AreaPlazaDetails(APIView):

    @swagger_auto_schema(responses={200: AreaPlazaSerializer})
    def get(self, request, pk):

        try:
            areaplaza = AreaPlaza.objects.get(pk=pk)
        except AreaPlaza.DoesNotExist:
            return Response({'error': 'Área de plaza no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AreaPlazaSerializer(areaplaza)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AreaPlazaSerializer, responses={200: AreaPlazaSerializer})
    def put(self, request, pk):

        try:
            areaplaza = AreaPlaza.objects.get(pk=pk)
        except AreaPlaza.DoesNotExist:
            return Response({'error': 'Área de plaza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AreaPlazaSerializer(areaplaza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AreaPlazaSerializer, responses={200: AreaPlazaSerializer})
    def patch(self, request, pk):

        try:
            areplaza = AreaPlaza.objects.get(pk=pk)
        except AreaPlaza.DoesNotExist:
            return Response({'error': 'Área de plaza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AreaPlazaSerializer(areplaza, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            areaplaza = AreaPlaza.objects.get(pk=pk)
        except AreaPlaza.DoesNotExist:
            return Response({'error': 'Área de plaza no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        areaplaza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)