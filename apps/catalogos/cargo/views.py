from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.cargo.models import Cargo
from .serializers import CargoSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permissions import CustomPermission
from Config.utils.pagination import PaginationMixin


# Create your views here.
class CargoAPIView(PaginationMixin, APIView):
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Cargo
    @swagger_auto_schema(responses={200: CargoSerializer(many=True)})
    def get(self, request):

        cargo = Cargo.objects.all().order_by('ID_Cargo')
        page= self.paginate_queryset(cargo, request)

        if page is not None:
            serializer = CargoSerializer(page, many=True)
            #logger.info("Paginated response for departamentos")
            return self.get_paginated_response(serializer.data)

        cargo = Cargo.objects.all()
        serializer = CargoSerializer(cargo, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CargoSerializer, responses={201: CargoSerializer})
    def post(self, request):

        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CargoDetails(APIView):

    @swagger_auto_schema(responses={200: CargoSerializer})
    def get(self, request, pk):

        try:
            cargo = Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            return Response({'error': 'Cargo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CargoSerializer(cargo)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CargoSerializer, responses={200: CargoSerializer})
    def put(self, request, pk):

        try:
            cargo = Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            return Response({'error': 'Cargo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CargoSerializer(cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CargoSerializer, responses={200: CargoSerializer})
    def patch(self, request, pk):

        try:
            cargo = Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            return Response({'error': 'Cargo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CargoSerializer(cargo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):

        try:
            cargo = Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            return Response({'error': 'Cargo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)