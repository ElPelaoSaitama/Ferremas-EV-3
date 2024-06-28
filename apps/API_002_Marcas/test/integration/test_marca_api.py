"""
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from apps.API_002_Marcas.models import Marca

@pytest.mark.django_db
class TestMarcaAPI:
    def test_creacion_marca_nombre_vacio(self):

        #Verifica que crear una marca con el nombre vacío retorna un error controlado.

        client = APIClient()
        url = reverse('marca-list-create')
        data = {'nombre': ''}
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'nombre' in response.data
        assert response.data['nombre'][0] == "Este campo no puede estar en blanco."

@pytest.mark.django_db
class TestMarcaAPI:
    def test_eliminar_marca_inexistente(self):

        #Verifica que eliminar una marca inexistente retorna un error controlado.

        client = APIClient()
        url = reverse('marca-detail', args=[9999])  # Asumiendo que 9999 no existe
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data['detail'] == "Marca no encontrada."
"""