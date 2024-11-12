from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import DepartamentoAPIView, DepartamentoDetails
from rest_framework.urls import app_name


app_name = "departamento"

urlpatterns = [
    path("", DepartamentoAPIView.as_view(), name="departamentos"),
    path('<int:pk>/', DepartamentoDetails.as_view()),
]
