import pytest
from apps.API_002_Marcas.models import Marca
from apps.API_002_Marcas.services import create_marca, get_marca, update_marca, delete_marca

@pytest.mark.django_db
class TestMarcaService:

    def test_create_marca(self):
        """
        Prueba para verificar que la función create_marca crea una marca correctamente.
        """
        marca = create_marca(nombre='MarcaTest')
        assert Marca.objects.filter(nombre='MarcaTest').exists()

    def test_get_marca(self):
        """
        Prueba para verificar que la función get_marca obtiene una marca correctamente.
        """
        marca = Marca.objects.create(nombre='MarcaGetTest')
        fetched_marca = get_marca(marca.id)
        assert fetched_marca.nombre == 'MarcaGetTest'

    def test_update_marca(self):
        """
        Prueba para verificar que la función update_marca actualiza una marca correctamente.
        """
        marca = Marca.objects.create(nombre='MarcaOldName')
        updated_marca = update_marca(marca, nombre='MarcaNewName')
        assert updated_marca.nombre == 'MarcaNewName'

    def test_delete_marca(self):
        """
        Prueba para verificar que la función delete_marca elimina una marca correctamente.
        """
        marca = Marca.objects.create(nombre='MarcaDeleteTest')
        delete_marca(marca)
        assert not Marca.objects.filter(nombre='MarcaDeleteTest').exists()
