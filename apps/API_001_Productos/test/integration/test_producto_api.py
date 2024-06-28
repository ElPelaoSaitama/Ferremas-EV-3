import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.API_001_Productos.models import Producto
from apps.API_002_Marcas.models import Marca
from apps.API_003_Categorias.models import Categoria

@pytest.mark.django_db
class TestProductoAPI:
    def test_crear_producto(self):
        """
        Prueba para validar que el endpoint de creación de productos funcione correctamente.
        """
        client = APIClient()
        # Crear instancias necesarias de Marca y Categoria
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        url = reverse('crear-producto')

        data = {
            'nombre': 'ProductoTest',
            'precio': 100,
            'descripcion': 'Descripción del producto Test',
            'nuevo': True,
            'marca': marca.id,
            'categoria': categoria.id,
            'imagen': None
        }

        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Producto.objects.count() == 1

    def test_listar_productos(self):
        """
        Prueba para validar que el endpoint de listar productos funcione correctamente.
        """
        client = APIClient()
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        Producto.objects.create(
            nombre='ProductoTest',
            precio=100,
            descripcion='Descripción del producto Test',
            nuevo=True,
            marca=marca,
            categoria=categoria,
            imagen=None
        )

        url = reverse('lista-productos')
        response = client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_obtener_detalle_producto(self):
        """
        Prueba para validar que el endpoint de obtener detalle de un producto funcione correctamente.
        """
        client = APIClient()
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        producto = Producto.objects.create(
            nombre='ProductoTest',
            precio=100,
            descripcion='Descripción del producto Test',
            nuevo=True,
            marca=marca,
            categoria=categoria,
            imagen=None
        )

        url = reverse('detalle-producto', args=[producto.id])
        response = client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['nombre'] == 'ProductoTest'



    def test_actualizar_producto(self):
        """
        Prueba para validar que el endpoint de actualizar un producto funcione correctamente.
        """
        client = APIClient()
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        producto = Producto.objects.create(
            nombre='ProductoTest',
            precio=100,
            descripcion='Descripción del producto Test',
            nuevo=True,
            marca=marca,
            categoria=categoria,
            imagen=None
        )

        url = reverse('detalle-producto', args=[producto.id])
        data = {
            'nombre': 'ProductoTestActualizado',
            'precio': 150,
            'descripcion': 'Descripción actualizada del producto Test',
            'nuevo': False,
            'marca': marca.id,
            'categoria': categoria.id,
            'imagen': None
        }

        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        producto.refresh_from_db()
        assert producto.nombre == 'ProductoTestActualizado'
        assert producto.precio == 150
        assert producto.descripcion == 'Descripción actualizada del producto Test'
        assert producto.nuevo is False
