from django.urls import path
from .api import LocalCreateAPIView, LocalListAPIView, LocalDetailAPIView

urlpatterns = [
    path('crear/', LocalCreateAPIView.as_view(), name='crear-local'),
    path('', LocalListAPIView.as_view(), name='lista-locales'),
    path('<int:pk>/', LocalDetailAPIView.as_view(), name='detalle-local'),
]
