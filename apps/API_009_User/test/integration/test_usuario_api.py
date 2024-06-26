import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
class TestUsuarioAPI:
    def test_user_registration_api_successfully(self):
        """
        Verifica que el registro de un nuevo usuario funcione correctamente.
        """
        client = APIClient()

        url = reverse('registro')

        data = {
            'username': 'usertest',
            'password': 'passwordtest'
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED

    def test_get_user_detail_api_successfully(self):
        """
        Verifica que se pueda obtener la informacion detallada de un usuario existente.
        """
        client = APIClient()

        user = User.objects.create_user(username='usertest', password='passwordtest')
        url = reverse('usuario-detalle', kwargs={'pk': user.pk})

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == 'usertest'

    def test_update_user_api_successfully(self):
        """
        Verifica que se pueda actualizar la informacion de un usuario existente.
        """
        client = APIClient()

        user = User.objects.create_user(username='usertest', password='passwordtest')
        url = reverse('usuario-detalle', kwargs={'pk': user.pk})

        data = {
            'username': 'usertest_updated'
        }

        response = client.put(url, data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == 'usertest_updated'

    def test_delete_user_api_successfully(self):
        """
        Verifica que se pueda eliminar un usuario existente.
        """
        client = APIClient()

        user = User.objects.create_user(username='usertest', password='passwordtest')
        url = reverse('usuario-detalle', kwargs={'pk': user.pk})

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not User.objects.filter(pk=user.pk).exists()

    def test_list_users_api_successfully(self):
        """
        Verifica que el se puede otener una lista de tofos los ususario registrados.
        """
        client = APIClient()

        User.objects.create_user(username='usertest1', password='passwordtest')
        User.objects.create_user(username='usertest2', password='passwordtest')
        url = reverse('usuarios-lista')

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
