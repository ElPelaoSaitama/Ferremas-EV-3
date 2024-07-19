from django.urls import path
from .api import (
    CarritoCreateAPIView, 
    CarritoDetailView, 
    ItemCarritoUpdateAPIView, 
    ItemCarritoDeleteAPIView
)

urlpatterns = [
    path('crear/', CarritoCreateAPIView.as_view(), name='crear-carrito'),
    path('<int:pk>/', CarritoDetailView.as_view(), name='detalle-carrito'),
    path('item/actualizar/<int:pk>/', ItemCarritoUpdateAPIView.as_view(), name='actualizar-item-carrito'),
    path('item/eliminar/<int:pk>/', ItemCarritoDeleteAPIView.as_view(), name='eliminar-item-carrito'),
]
