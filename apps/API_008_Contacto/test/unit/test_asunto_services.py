import pytest
from apps.API_008_Contacto.models import Asunto
from apps.API_008_Contacto.services import create_asunto, delete_asunto, get_asunto, update_asunto

@pytest.mark.django_db
class TestAsuntoService:
    def test_create_asunt_succesfully(self):
        """
        Validacion del metodo para crear asunto correctamente
        """
        # Creacion de un nuevo asunto
        asunto = create_asunto('testAsunto')

        # Verificar que el asunto se ha creado correctamente
        assert asunto.nombre == 'testAsunto'
    
    def test_delete_asunt_successfully(self):
        # Creamos un nuevo asunto para eliminarlo posteriormente
        asunto = create_asunto('testAsunto')

        # Eliminamos nuestro asunto
        delete_asunto(asunto)

        # Validar que el asunto ya no exista dentro de la base de datos de prueba
        with pytest.raises(Asunto.DoesNotExist):
            get_asunto(asunto.id)