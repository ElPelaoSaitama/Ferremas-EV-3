import pytest
from apps.API_008_Contacto.models import Asunto, Contacto
from apps.API_008_Contacto.services import create_contacto, get_contacto, update_contacto, delete_contacto

@pytest.mark.django_db
class TestContactoService:
    def test_create_contacto_successfully(self):
        """
        Validar que el método create_contacto funcione correctamente.
        """
        # Creamos un asunto para asociarlo al contacto
        asunto = Asunto.objects.create(nombre="Consulta")
        
        # Creamos un nuevo contacto
        contacto = create_contacto(
            nombre='Carlos Martinez',
            email='carlos.martinez@example.com',
            telefono='0987654321',
            mensaje='Nuevo mensaje de prueba',
            asunto=asunto
        )

        # Verificamos que el contacto creado tenga el mismo email que usamos para crearlo
        assert contacto.email == 'carlos.martinez@example.com'

    def test_get_contacto_successfully(self):
        """
        Validar que el método get_contacto funcione correctamente.
        """
        # Creamos un asunto y un contacto
        asunto = Asunto.objects.create(nombre="Consulta")
        contacto_creado = Contacto.objects.create(
            nombre='Juan Perez',
            email='juan.perez@example.com',
            telefono='1234567890',
            mensaje='Mensaje de prueba',
            asunto=asunto
        )

        # Obtenemos el contacto creado
        contacto_obtenido = get_contacto(contacto_creado.id)

        # Verificamos que el contacto obtenido tenga el mismo email que el creado
        assert contacto_obtenido.email == 'juan.perez@example.com'

    def test_update_contacto_successfully(self):
        """
        Validar que el método update_contacto funcione correctamente.
        """
        # Creamos un asunto y un contacto
        asunto = Asunto.objects.create(nombre="Consulta")
        contacto = Contacto.objects.create(
            nombre='Juan Perez',
            email='juan.perez@example.com',
            telefono='1234567890',
            mensaje='Mensaje de prueba',
            asunto=asunto
        )

        # Actualizamos el contacto
        contacto_actualizado = update_contacto(
            contacto.id,
            nombre='Juan Perez Actualizado',
            email='juan.perez@example.com',
            telefono='1234567890',
            mensaje='Mensaje de prueba actualizado',
            asunto=asunto
        )

        # Verificamos que los datos hayan sido actualizados correctamente
        assert contacto_actualizado.nombre == 'Juan Perez Actualizado'
        assert contacto_actualizado.mensaje == 'Mensaje de prueba actualizado'

    def test_delete_contacto_successfully(self):
        """
        Validar que el método delete_contacto funcione correctamente.
        """
        # Creamos un asunto y un contacto
        asunto = Asunto.objects.create(nombre="Consulta")
        contacto = Contacto.objects.create(
            nombre='Juan Perez',
            email='juan.perez@example.com',
            telefono='1234567890',
            mensaje='Mensaje de prueba',
            asunto=asunto
        )

        # Eliminamos el contacto
        delete_contacto(contacto)

        # Verificamos que el contacto ya no exista en la base de datos
        with pytest.raises(Contacto.DoesNotExist):
            get_contacto(contacto.id)
