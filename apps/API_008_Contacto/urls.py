from django.urls import path
from .api import AsuntoCreateAPIView, AsuntoDetailAPIView, AsuntoListAPIView
from .api import ContactoCreateAPIView, ContactoDetailAPIView, ContactoListAPIView
urlpatterns = [
    # Urls Flujo Asunto
    path('asunto/', AsuntoListAPIView.as_view(), name="asunto-list"),
    path('asunto/crear/', AsuntoCreateAPIView.as_view(), name="asunto-create"),
    path('asunto/<int:pk>/', AsuntoDetailAPIView.as_view(), name="asunto-detail"),

    # Urls Flujo Contacto
    path('contacto/', ContactoListAPIView.as_view(), name="contacto-list"),
    path('contacto/crear/', ContactoCreateAPIView.as_view(), name="contacto-create"),
    path('contacto/<int:pk>/', ContactoDetailAPIView.as_view(), name="contacto-detail")
]
