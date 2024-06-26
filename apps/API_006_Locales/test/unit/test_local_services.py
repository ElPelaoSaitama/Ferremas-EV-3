import pytest
from apps.API_006_Locales.models import Local
from apps.API_006_Locales.services import crear_local, obtener_local, actualizar_local, eliminar_local

@pytest.mark.django_db
class TestLocalService:

    def test_crear_local_exitosamente(self):
        """
        Prueba para validar que el método crear_local funcione correctamente.
        """
        local = crear_local(
            nombre="Local Test",
            direccion="Direccion Test",
            telefono="123456789",
            email="local@test.com",
            horario_apertura="08:00:00",
            horario_cierre="17:00:00"
        )
        assert local.nombre == "Local Test"
        assert Local.objects.count() == 1

    def test_obtener_local_exitosamente(self):
        """
        Prueba para validar que el método obtener_local funcione correctamente.
        """
        local = crear_local(
            nombre="Local Test",
            direccion="Direccion Test",
            telefono="123456789",
            email="local@test.com",
            horario_apertura="08:00:00",
            horario_cierre="17:00:00"
        )
        fetched_local = obtener_local(local.id)
        assert fetched_local == local

    def test_actualizar_local_exitosamente(self):
        """
        Prueba para validar que el método actualizar_local funcione correctamente.
        """
        local = crear_local(
            nombre="Local Test",
            direccion="Direccion Test",
            telefono="123456789",
            email="local@test.com",
            horario_apertura="08:00:00",
            horario_cierre="17:00:00"
        )
        updated_local = actualizar_local(local, nombre="Nuevo Nombre")
        assert updated_local.nombre == "Nuevo Nombre"

    def test_eliminar_local_exitosamente(self):
        """
        Prueba para validar que el método eliminar_local funcione correctamente.
        """
        local = crear_local(
            nombre="Local Test",
            direccion="Direccion Test",
            telefono="123456789",
            email="local@test.com",
            horario_apertura="08:00:00",
            horario_cierre="17:00:00"
        )
        eliminar_local(local)
        with pytest.raises(Local.DoesNotExist):
            obtener_local(local.id)
