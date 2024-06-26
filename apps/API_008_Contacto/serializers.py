from rest_framework import serializers
from apps.API_008_Contacto.models import Asunto, Contacto
from apps.API_008_Contacto.services import create_asunto, create_contacto

class AsuntoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asunto
        fields = ['id', 'nombre']
    
    def create(self, validated_data):
        return create_asunto(**validated_data)

class ContactoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['id','asunto', 'nombre', 'email', 'telefono', 'mensaje']

    def create(self, validated_data):
        return create_contacto(**validated_data)