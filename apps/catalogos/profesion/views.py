from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.profesion.models import Profesion
from .serializers import ProfesionSerializer
from drf_yasg.utils import swagger_auto_schema
from Config.utils.pagination import PaginationMixin

# Create your views here.
class ProfesionAPIView(PaginationMixin, APIView):

    @swagger_auto_schema(responses={200: ProfesionSerializer(many=True)})
    def get(self, request):

        profesion = Profesion.objects.all().order_by('ID_Profesion')
        page = self.paginate_queryset(profesion, request)

        if page is not None:
            serializer = ProfesionSerializer(page, many=True)
            # logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        profesion = Profesion.objects.all()
        serializer = ProfesionSerializer(profesion, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProfesionSerializer, responses={201: ProfesionSerializer})
    def post(self, request):

        serializer = ProfesionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfesionDetails(APIView):


    @swagger_auto_schema(responses={200: ProfesionSerializer})
    def get(self, request, pk):

        try:
            profesion = Profesion.objects.get(pk=pk)
        except Profesion.DoesNotExist:
            return Response({'error': 'Profesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProfesionSerializer(profesion)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProfesionSerializer, responses={200: ProfesionSerializer})
    def put(self, request, pk):

        try:
            profesion = Profesion.objects.get(pk=pk)
        except Profesion.DoesNotExist:
            return Response({'error': 'Profesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfesionSerializer(profesion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ProfesionSerializer, responses={200: ProfesionSerializer})
    def patch(self, request, pk):

        try:
            profesion = Profesion.objects.get(pk=pk)
        except Profesion.DoesNotExist:
            return Response({'error': 'Profesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfesionSerializer(profesion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            profesion = Profesion.objects.get(pk=pk)
        except Profesion.DoesNotExist:
            return Response({'error': 'Profesión no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        profesion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)