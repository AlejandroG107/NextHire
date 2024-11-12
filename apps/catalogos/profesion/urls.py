from django.urls import path
from .views import ProfesionAPIView, ProfesionDetails

app_name= "profesion"

urlpatterns = [
    path("", ProfesionAPIView.as_view(), name="profesion"),
    path('<int:pk>/', ProfesionDetails.as_view()),
]