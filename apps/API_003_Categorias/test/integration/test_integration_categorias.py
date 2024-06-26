import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.API_003_Categorias.models import Categoria

@pytest.mark.django_db
class TestCategoriaAPI:

    def test_create_categoria(self):
        """
         Verifica que se pueda crear una nueva categoría enviando datos válidos a través de una solicitud POST a la URL de creación de categorías (categoria-create). 
         Se asegura de que se devuelva el código de estado 201 CREATED y de que la categoría se haya creado correctamente en la base de datos.
        """
        client = APIClient()
        url = reverse('categoria-create')
        data = {'nombre': 'Herramientas'}

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert Categoria.objects.filter(nombre='Herramientas').exists()

    def test_get_categoria(self):
        """
         Verifica que se pueda obtener una categoría existente utilizando su id a través de una solicitud GET a la URL de detalle de categorías (categoria-detail). 
         Se asegura de que se devuelva el código de estado 200 OK y de que los datos de la categoría obtenida sean correctos.
        """
        categoria = Categoria.objects.create(nombre='Electricidad')
        client = APIClient()
        url = reverse('categoria-detail', kwargs={'pk': categoria.id})

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['nombre'] == 'Electricidad'

    def test_update_categoria(self):
        """
        Verifica que se pueda actualizar una categoría existente enviando datos actualizados a través de una solicitud PUT a la URL de detalle de categorías (categoria-detail). 
        Se asegura de que se devuelva el código de estado 200 OK y de que la categoría se haya actualizado correctamente en la base de datos.
        """
        categoria = Categoria.objects.create(nombre='Jardinería')
        client = APIClient()
        url = reverse('categoria-detail', kwargs={'pk': categoria.id})
        updated_data = {'nombre': 'Jardinería y Paisajismo'}

        response = client.put(url, updated_data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert Categoria.objects.get(id=categoria.id).nombre == 'Jardinería y Paisajismo'

    def test_delete_categoria(self):
        """
        Verifica que se pueda eliminar una categoría existente a través de una solicitud DELETE a la URL de detalle de categorías (categoria-detail). 
        Se asegura de que se devuelva el código de estado 204 NO CONTENT y de que la categoría se haya eliminado correctamente de la base de datos.
        """
        categoria = Categoria.objects.create(nombre='Ferretería')
        client = APIClient()
        url = reverse('categoria-detail', kwargs={'pk': categoria.id})

        response = client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Categoria.objects.filter(id=categoria.id).exists()
