from django.urls import path
from .views import ArePlazaAPIView, AreaPlazaDetails

app_name = "area_plaza"

urlpatterns = [
    path("", ArePlazaAPIView.as_view(), name="area_plaza"),
    path('<int:pk>/', AreaPlazaDetails.as_view()),
    ]