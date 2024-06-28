import pytest
from django.contrib.auth.models import User

from apps.API_009_User.services import create_user, delete_user, get_user, update_user


@pytest.mark.django_db
class TestUsuarioService:
    def test_create_user_succesfully(self):
        """
        validar que el método crear usuario funcione correctamente.
        """
        # Creamos un usuario nuevo
        user = create_user('testuser', 'testpassword')
        
        # Verificamos que el usuario creado tenga el mismo username que usamos para crearlo
        assert user.username == 'testuser'

        # Verificamos con el método check_password que la contrase;a sea correcta
        assert user.check_password('testpassword') is True
        
    def test_delete_user_successfully(self):
        """
        Validar que el metodo delete_user funcione correctamente.
        """
        # Creamos un usuario nuevo para eliminarlo posteriormente
        user = create_user('testuser', 'testpassword')

        # Eliminamos nuestro usuario
        delete_user(user)

        # Validamos que el usuario ya no exista dentro de nuestra base de datos de prueba
        with pytest.raises(User.DoesNotExist):
            get_user(user.id)

    def test_get_user_successfully(self):
        """
        Validar que el método obtener usuario funcione correctamente.
        """
        # Creamos un usuario nuevo
        user = create_user('testuser', 'testpassword')

        # Obtenemos el usuario usando el ID
        retrieved_user = get_user(user.id)

        # Validamos que el usuario obtenido sea el mismo que creamos
        assert retrieved_user.username == 'testuser'

    def test_get_user_not_exist(self):
        """
        Validar que el método obtener usuario maneje el caso de usuario no existente.
        """
        # Intentamos obtener un usuario que no existe
        with pytest.raises(User.DoesNotExist):
            get_user(9999)

    def test_update_user_successfully(self):
        """
        Validar que el método actualizar usuario funcione correctamente.
        """
        # Creamos un usuario nuevo
        user = create_user('testuser', 'testpassword')

        # Actualizamos el username del usuario
        updated_user = update_user(user, username='updateduser')

        # Verificamos que el username haya sido actualizado
        assert updated_user.username == 'updateduser'

    def test_update_user_without_changes(self):
        """
        Validar que el método actualizar usuario maneje el caso de no hacer cambios.
        """
        # Creamos un usuario nuevo
        user = create_user('testuser', 'testpassword')

        # Actualizamos el usuario sin hacer cambios
        updated_user = update_user(user)

        # Verificamos que el username siga siendo el mismo
        assert updated_user.username == 'testuser'

    def test_delete_user_not_exist(self):
        """
        Validar que el método eliminar usuario maneje el caso de usuario no existente.
        """
        # Creamos un usuario nuevo y lo eliminamos
        user = create_user('testuser', 'testpassword')
        delete_user(user)

        # Intentamos eliminar nuevamente el mismo usuario
        with pytest.raises(User.DoesNotExist):
            delete_user(user)

    def test_update_user_not_exist(self):
        """
        Validar que el método actualizar usuario maneje el caso de usuario no existente.
        """
        # Creamos un usuario nuevo y lo eliminamos
        user = create_user('testuser', 'testpassword')
        delete_user(user)

        # Intentamos actualizar el usuario eliminado
        with pytest.raises(User.DoesNotExist):
            update_user(user, username='newusername')
