import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.API_008_Contacto.models import Asunto

@pytest.mark.django_db
class TestAsuntoAPI:
    def test_asunto_registration_api_successfully(self):
        """
        Se debe probar que se puede crear un asutno por medio de la API
        """
        client = APIClient()

        url = reverse('asunto-create')

        data = {
            'nombre': 'AsuntoTest'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
    
    def test_get_asunto_no_existente(self):
        """
        Se debe probar el error al hacer un get hacia un asunto_id no existente
        """
        client = APIClient()
        url = reverse('contacto-detail',kwargs={'pk': 200})

        response = client.get(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_asunto_crear_sin_datos(self):
        """
        Se debe validar de que no se cree el asunto si no tene texto
        """
        client = APIClient()
        url = reverse('asunto-create')

        data = {
            'nombre': ''
        }

        response = client.post(url, data, follow='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_asunto_eliminar_no_exustente(self):
        """
        Se debe validar el error controlado al intentar eliminar un asunto_id que no existe
        """
        client = APIClient()
        url = reverse('contacto-detail', kwargs={'pk': 200})

        response = client.delete(url)

        assert response.status_code == status.HTTP_404_NOT_FOUND
        