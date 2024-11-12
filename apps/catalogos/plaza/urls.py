from django.urls import path
from .views import PlazaAPIView, DetallePlazaDetails

app_name= "plaza"

urlpatterns = [
    path('', PlazaAPIView.as_view(), name='plaza'),
    path('<int:pk>/', DetallePlazaDetails.as_view()),
]