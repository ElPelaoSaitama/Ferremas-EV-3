from django.urls import path
from .api import OrdenCreateAPIView, OrdenDetailAPIView, OrdenListAPIView

urlpatterns = [
    path('ordenes/', OrdenListAPIView.as_view(), name='lista-ordenes'),
    path('ordenes/crear/', OrdenCreateAPIView.as_view(), name='crear-orden'),
    path('ordenes/<int:pk>/', OrdenDetailAPIView.as_view(), name='detalle-orden'),
]
