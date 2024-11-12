from django.urls import path
from .views import UsersAPIView

urlpatterns = [
   path("", UsersAPIView.as_view(), name="usuarios"),
]