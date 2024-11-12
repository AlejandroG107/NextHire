from django.urls import path
from .views import MunicipioAPIView, MunicipioDetails
from ..departamentos.urls import app_name

app_name= "Municipio"

urlpatterns = [
    path('', MunicipioAPIView.as_view(), name='municipio'),
    path('<int:pk>/', MunicipioDetails.as_view()),
]