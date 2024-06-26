import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.API_006_Locales.models import Local

@pytest.mark.django_db
class TestLocalAPI:
    def test_crear_local_api_exitosamente(self):
        """
        Prueba para validar que el endpoint de creación de locales funcione correctamente.
        """
        client = APIClient()
        url = reverse('crear-local')
        data = {
            'nombre': 'Local Test',
            'direccion': 'Direccion Test',
            'telefono': '123456789',
            'email': 'local@test.com',
            'horario_apertura': '08:00:00',
            'horario_cierre': '17:00:00'
        }
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Local.objects.count() == 1

    def test_listar_locales_api_exitosamente(self):
        """
        Prueba para validar que el endpoint de listar locales funcione correctamente.
        """
        client = APIClient()
        Local.objects.create(
            nombre='Local Test',
            direccion='Direccion Test',
            telefono='123456789',
            email='local@test.com',
            horario_apertura='08:00:00',
            horario_cierre='17:00:00'
        )
        url = reverse('lista-locales')
        response = client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_obtener_detalle_local_api_exitosamente(self):
        """
        Prueba para validar que el endpoint de obtener detalle de un local funcione correctamente.
        """
        client = APIClient()
        local = Local.objects.create(
            nombre='Local Test',
            direccion='Direccion Test',
            telefono='123456789',
            email='local@test.com',
            horario_apertura='08:00:00',
            horario_cierre='17:00:00'
        )
        url = reverse('detalle-local', args=[local.id])
        response = client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['nombre'] == 'Local Test'

    def test_actualizar_local_api_exitosamente(self):
        """
        Prueba para validar que el endpoint de actualizar un local funcione correctamente.
        """
        client = APIClient()
        local = Local.objects.create(
            nombre='Local Test',
            direccion='Direccion Test',
            telefono='123456789',
            email='local@test.com',
            horario_apertura='08:00:00',
            horario_cierre='17:00:00'
        )
        url = reverse('detalle-local', args=[local.id])
        data = {
            'nombre': 'Nuevo Nombre',
            'direccion': 'Direccion Test',
            'telefono': '123456789',
            'email': 'local@test.com',
            'horario_apertura': '08:00:00',
            'horario_cierre': '17:00:00'
        }
        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        local.refresh_from_db()
        assert local.nombre == 'Nuevo Nombre'
