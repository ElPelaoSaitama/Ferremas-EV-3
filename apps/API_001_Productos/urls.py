from django.urls import path
from .api import ProductoCreateAPIView, ProductoDetailAPIView, ProductoListAPIView

urlpatterns = [
    path('listar/', ProductoListAPIView.as_view(), name="lista-productos"),
    path('crear/', ProductoCreateAPIView.as_view(), name="crear-producto"),
    path('<int:pk>/', ProductoDetailAPIView.as_view(), name="detalle-producto"),
]
