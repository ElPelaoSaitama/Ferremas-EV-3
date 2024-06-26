from django.test import TestCase
from apps.API_001_Productos.models import Producto
from apps.API_001_Productos.services import crear_producto, actualizar_producto, eliminar_producto
from apps.API_002_Marcas.models import Marca
from apps.API_003_Categorias.models import Categoria

class ProductoServiceTests(TestCase):

    def setUp(self):
        # Configuración de datos comunes para las pruebas
        self.marca = Marca.objects.create(nombre="Marca1")
        self.categoria = Categoria.objects.create(nombre="Categoria1")
        self.producto = crear_producto(
            nombre="Producto1",
            precio=100,
            descripcion="Descripción del producto 1",
            nuevo=True,
            marca=self.marca,
            categoria=self.categoria
        )

    def test_crear_producto_service(self):
        # Prueba del servicio de creación de productos
        producto = crear_producto(
            nombre="Producto2",
            precio=200,
            descripcion="Descripción del producto 2",
            nuevo=True,
            marca=self.marca,
            categoria=self.categoria
        )
        self.assertIsInstance(producto, Producto)
        self.assertEqual(producto.nombre, "Producto2")
        self.assertEqual(producto.precio, 200)
        self.assertEqual(producto.descripcion, "Descripción del producto 2")
        self.assertTrue(producto.nuevo)
        self.assertEqual(producto.marca, self.marca)
        self.assertEqual(producto.categoria, self.categoria)

    def test_actualizar_producto_service(self):
        # Prueba del servicio de actualización de productos
        updated_producto = actualizar_producto(
            producto_id=self.producto.id,
            nombre="Producto1 Actualizado",
            precio=150,
            descripcion="Descripción actualizada",
            nuevo=False,
            marca=self.marca,
            categoria=self.categoria
        )
        self.assertEqual(updated_producto.nombre, "Producto1 Actualizado")
        self.assertEqual(updated_producto.precio, 150)
        self.assertEqual(updated_producto.descripcion, "Descripción actualizada")
        self.assertFalse(updated_producto.nuevo)

    def test_eliminar_producto_service(self):
        # Prueba del servicio de eliminación de productos
        producto_id = self.producto.id
        eliminar_producto(producto_id)
        with self.assertRaises(Producto.DoesNotExist):
            Producto.objects.get(id=producto_id)

    def test_recuperar_producto_service(self):
        # Prueba del servicio de recuperación de productos
        producto_recuperado = Producto.objects.get(id=self.producto.id)
        self.assertEqual(producto_recuperado.nombre, "Producto1")
        self.assertEqual(producto_recuperado.precio, 100)
        self.assertEqual(producto_recuperado.descripcion, "Descripción del producto 1")
        self.assertTrue(producto_recuperado.nuevo)
        self.assertEqual(producto_recuperado.marca, self.marca)
        self.assertEqual(producto_recuperado.categoria, self.categoria)
