from django.urls import path
from .views import EmpresaAPIView, EmpresaDetails

app_name = "empresa"

urlpatterns = [
    path("", EmpresaAPIView.as_view(), name="empresa"),
    path('<int:pk>/', EmpresaDetails.as_view()),
]