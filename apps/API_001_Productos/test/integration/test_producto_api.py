import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from apps.API_001_Productos.models import Producto
from apps.API_002_Marcas.models import Marca
from apps.API_003_Categorias.models import Categoria

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def marca():
    return Marca.objects.create(nombre='Marca1')

@pytest.fixture
def categoria():
    return Categoria.objects.create(nombre='Categoria1')

@pytest.mark.django_db
class TestProductoAPI:

    def test_create_product_name_invalid(api_client, marca, categoria):
        client = APIClient
        url = reverse('crear-producto')

        data = {
            'nombre': 'aa',
            'precio': 1,
            'descripcion': 'descripcion',
            'nuevo': True,
            'marca': marca.id,
            'categoria': categoria.id,
            'imagen': None
        }

        response = client.post(url, data, format='json')

        assert response.status_code == status.HTTP_201_CREATED









"""

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from apps.API_001_Productos.models import Producto
from apps.API_002_Marcas.models import Marca
from apps.API_003_Categorias.models import Categoria


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def marca():
    return Marca.objects.create(nombre='Marca1')

@pytest.fixture
def categoria():
    return Categoria.objects.create(nombre='Categoria1')


@pytest.mark.django_db
def test_crear_producto(api_client, marca, categoria):
    # Prueba de integración para crear un producto.
    url = '/api/productos/crear/'
    data = {
        "nombre": "Producto1",
        "precio": 100,
        "descripcion": "Descripción del producto 1",
        "nuevo": True,
        "marca": marca.id,
        "categoria": categoria.id,
        "imagen": None
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert Producto.objects.count() == 1

@pytest.mark.django_db
def test_obtener_producto(api_client, marca, categoria):
    # Prueba de integración para obtener un producto.
    producto = Producto.objects.create(
        nombre="Producto1",
        precio=100,
        descripcion="Descripción del producto 1",
        nuevo=True,
        marca=marca,
        categoria=categoria
    )
    url = f'/api/productos/{producto.id}/'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['nombre'] == "Producto1"

@pytest.mark.django_db
def test_actualizar_producto(api_client, marca, categoria):
    # Prueba de integración para actualizar un producto.
    producto = Producto.objects.create(
        nombre="Producto1",
        precio=100,
        descripcion="Descripción del producto 1",
        nuevo=True,
        marca=marca,
        categoria=categoria
    )
    url = f'/api/productos/{producto.id}/'
    data = {
        "nombre": "Producto1 actualizado",
        "precio": 150,
        "descripcion": "Descripción actualizada",
        "nuevo": False,
        "marca": marca.id,
        "categoria": categoria.id,
        "imagen": None
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    producto.refresh_from_db()
    assert producto.nombre == "Producto1 actualizado"
    assert producto.precio == 150

@pytest.mark.django_db
def test_eliminar_producto(api_client, marca, categoria):
    #Prueba de integración para eliminar un producto.
    producto = Producto.objects.create(
        nombre="Producto1",
        precio=100,
        descripcion="Descripción del producto 1",
        nuevo=True,
        marca=marca,
        categoria=categoria
    )
    url = f'/api/productos/{producto.id}/'
    response = api_client.delete(url)
    assert response.status_code == 204
    assert Producto.objects.count() == 0

"""
