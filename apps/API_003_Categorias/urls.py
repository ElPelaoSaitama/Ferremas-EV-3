from django.urls import path
from .api import CategoriaCreateAPIView, CategoriaDetailAPIView, CategoriaListAPIView

urlpatterns = [
    path('', CategoriaListAPIView.as_view(), name="categoria-list"),
    path('crear/', CategoriaCreateAPIView.as_view(), name="categoria-create"),
    path('<int:pk>/', CategoriaDetailAPIView.as_view(), name="categoria-detail"),
]
