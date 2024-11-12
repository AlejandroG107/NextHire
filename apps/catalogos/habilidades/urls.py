from django.urls import path
from .views import HabilidadesAPIView, DetalleHabilidadDetails

app_name= "habilidades"

urlpatterns = [
    path('', HabilidadesAPIView.as_view(), name='habilidades'),
    path('<int:pk>/', DetalleHabilidadDetails.as_view()),
]