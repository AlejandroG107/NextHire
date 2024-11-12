from django.urls import path
from .views import PostulanteAPIView, DetallePostulanteDetails

app_name= "postulante"

urlpatterns = [
    path('', PostulanteAPIView.as_view(), name='postulantes'),
    path('<int:pk>/', DetallePostulanteDetails.as_view()),
]