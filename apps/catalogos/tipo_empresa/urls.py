from django.urls import path
from .views import TipoEmpresaAPIView, TipoEmpresaDetails

app_name = "tipo_empresa"


urlpatterns = [
    path("", TipoEmpresaAPIView.as_view(), name="tipo_empresa"),
    path('<int:pk>/', TipoEmpresaDetails.as_view()),
]