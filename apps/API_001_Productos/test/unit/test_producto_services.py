import pytest
from django.core.exceptions import ObjectDoesNotExist
from apps.API_001_Productos.models import Producto
from apps.API_002_Marcas.models import Marca
from apps.API_003_Categorias.models import Categoria
from apps.API_001_Productos.services import crear_producto, actualizar_producto, eliminar_producto

@pytest.mark.django_db
class TestProductoService:
    def test_crear_producto(self):
        """
        Prueba para validar que el método crear_producto funcione correctamente.
        """
        # Crear instancias necesarias de Marca y Categoria
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        data = {
            'nombre': 'ProductoTest',
            'precio': 100,
            'descripcion': 'Descripción del producto Test',
            'nuevo': True,
            'marca': marca,
            'categoria': categoria,
            'imagen': None
        }

        # Llamar al servicio de creación de producto
        producto = crear_producto(**data)

        # Verificar que el producto se haya creado correctamente
        assert producto.nombre == 'ProductoTest'
        assert producto.precio == 100
        assert producto.descripcion == 'Descripción del producto Test'
        assert producto.nuevo is True
        assert producto.marca == marca
        assert producto.categoria == categoria

    def test_actualizar_producto(self):
        """
        Prueba para validar que el método actualizar_producto funcione correctamente.
        """
        # Crear instancias necesarias de Marca y Categoria
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        # Crear un producto existente
        producto = Producto.objects.create(
            nombre='ProductoTest',
            precio=100,
            descripcion='Descripción del producto Test',
            nuevo=True,
            marca=marca,
            categoria=categoria,
            imagen=None
        )

        data_actualizada = {
            'nombre': 'ProductoTestActualizado',
            'precio': 150,
            'descripcion': 'Descripción actualizada del producto Test',
            'nuevo': False,
            'marca': marca,
            'categoria': categoria,
            'imagen': None
        }

        # Llamar al servicio de actualización de producto
        producto_actualizado = actualizar_producto(producto.id, **data_actualizada)

        # Verificar que el producto se haya actualizado correctamente
        assert producto_actualizado.nombre == 'ProductoTestActualizado'
        assert producto_actualizado.precio == 150
        assert producto_actualizado.descripcion == 'Descripción actualizada del producto Test'
        assert producto_actualizado.nuevo is False

    def test_eliminar_producto(self):
        """
        Prueba para validar que el método eliminar_producto funcione correctamente.
        """
        # Crear instancias necesarias de Marca y Categoria
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        # Crear un producto existente
        producto = Producto.objects.create(
            nombre='ProductoTest',
            precio=100,
            descripcion='Descripción del producto Test',
            nuevo=True,
            marca=marca,
            categoria=categoria,
            imagen=None
        )

        # Llamar al servicio de eliminación de producto
        eliminar_producto(producto.id)

        # Verificar que el producto se haya eliminado correctamente
        with pytest.raises(Producto.DoesNotExist):
            Producto.objects.get(id=producto.id)

    def test_actualizar_producto_id_no_encontrado(self):
        """
        Prueba para validar que el método actualizar_producto maneje correctamente el caso 
        cuando se intenta actualizar un producto con un ID que no existe.
        """
        # Crear instancias necesarias de Marca y Categoria
        marca = Marca.objects.create(nombre='MarcaTest')
        categoria = Categoria.objects.create(nombre='CategoriaTest')

        data_actualizada = {
            'nombre': 'ProductoTestActualizado',
            'precio': 150,
            'descripcion': 'Descripción actualizada del producto Test',
            'nuevo': False,
            'marca': marca,
            'categoria': categoria,
            'imagen': None
        }

        # Usar un ID que no existe
        id_no_existente = 9999

        # Intentar actualizar el producto y verificar que se lance una excepción
        with pytest.raises(ValueError) as excinfo:
            actualizar_producto(id_no_existente, **data_actualizada)