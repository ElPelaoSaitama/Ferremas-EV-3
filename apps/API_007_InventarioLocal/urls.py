from django.urls import path
from .api import InventarioLocalDetailAPIView, InventarioLocalCreateAPIVew

urlpatterns = [
    path('inventarios/', InventarioLocalCreateAPIVew.as_view(), name="lista-inventarios"),
    #path('inventarios/crear/', InventarioLocalCreateAPIView.as_view(), name="crear-inventario"),
    #path('inventarios/<int:pk>/', InventarioLocalDetailAPIView.as_view(), name="detalle-inventario"),
]
