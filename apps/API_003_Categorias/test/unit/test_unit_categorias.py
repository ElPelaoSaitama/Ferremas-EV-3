import pytest
from django.contrib.auth.models import User
from apps.API_003_Categorias.models import Categoria
from apps.API_003_Categorias.services import create_categoria, get_categoria, update_categoria, delete_categoria

@pytest.mark.django_db
class TestCategoriaService:

    def test_crear_categoria(self):
        """
        Verifica que el método create_categoria pueda crear una nueva categoría en la base de datos y que exista correctamente.
        """
        categoria = create_categoria('Herramientas')
        assert categoria is not None
        assert Categoria.objects.filter(nombre='Herramientas').exists()

    def test_obtener_categoria(self):
        """
        Verifica que el método get_categoria pueda recuperar una categoría existente según su id y que los datos obtenidos sean correctos.
        """
        categoria_creada = Categoria.objects.create(nombre='Electricidad')
        categoria_obtenida = get_categoria(categoria_creada.id)
        assert categoria_obtenida is not None
        assert categoria_obtenida.nombre == 'Electricidad'

    def test_actualizar_categoria(self):
        """
        Verifica que el método update_categoria pueda actualizar los datos de una categoría existente y que los cambios se reflejen correctamente en la base de datos.
        """
        categoria_creada = Categoria.objects.create(nombre='Jardinería')
        categoria_actualizada = update_categoria(categoria_creada, nombre='Jardinería y Paisajismo')
        assert categoria_actualizada is not None
        assert categoria_actualizada.nombre == 'Jardinería y Paisajismo'

    def test_eliminar_categoria(self):
        """
        Verifica que el método delete_categoria pueda eliminar una categoría existente de la base de datos y que ya no esté disponible al intentar obtenerla posteriormente.
        """
        categoria_creada = Categoria.objects.create(nombre='Ferretería')
        delete_categoria(categoria_creada)
        with pytest.raises(Categoria.DoesNotExist):
            Categoria.objects.get(id=categoria_creada.id)
