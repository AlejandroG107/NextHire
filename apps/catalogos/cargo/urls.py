from django.urls import path
from .views import CargoAPIView, CargoDetails

app_name = "cargo"

urlpatterns = [
    path("", CargoAPIView.as_view(), name="cargo"),
    path('<int:pk>/', CargoDetails.as_view()),
]