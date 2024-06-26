from django.urls import path

from .api import UserCreateAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('registrar/', UserCreateAPIView.as_view(), name="registro"),
    path('usuarios/', UserListAPIView.as_view(), name="usuarios-lista"),
    path('usuarios/<int:pk>/', UserDetailAPIView.as_view(), name="usuario-detalle"),
    path('usuarios/eliminar/<int:pk>/', UserListAPIView.as_view(), name="usuarios-eliminar"),
]