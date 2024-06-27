import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from apps.API_008_Contacto.models import Asunto, Contacto

@pytest.mark.django_db
class TestContactoAPI:
    def test_contacto_vacio(self):
        """
        Verificar que no se cree una solicitud de contacto enviando datos vacios
        """
        client = APIClient()

        url = reverse('contacto-create')

        data = {
            'asunto': None,
            'nombre': '',
            'email': '',
            'telefono': '',
            'mensaje': ''
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_contacto_formato_email_incorrecto(self):
        """
        Verificar que no se cree el contacto si se ingresa un email con formato incorrecto
        """

        client = APIClient()
        url = reverse('contacto-create')

        data = {
            'asunto': 1,
            'nombre': 'ContactoTest',
            'email': 'EmailIncorrecto',
            'telefono': '123',
            'mensaje': 'MensajeTest'
        }

        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_contacto_asunto_no_existe(self):
        """
        Verificar que no se cree el contacto si se ingresa un asunto_id que no existe
        """

        client = APIClient()
        url = reverse('contacto-create')

        data = {
            'asunto': 1000,
            'nombre': 'ContactoTest',
            'email': 'Email@test.cl',
            'telefono': '123',
            'mensaje': 'MensajeTest'
        }

        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_contacto_recuperar_contacto_inexistente(self):
        """
        Verificar que se controle el error al traer un contacto_id que no existe en la db
        """
        client = APIClient()
        url = reverse('contacto-detail', kwargs={'pk': 200})

        response = client.get(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST