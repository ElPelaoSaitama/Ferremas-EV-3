from rest_framework import serializers
from apps.API_003_Categorias.models import Categoria
from .services import create_categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

    def create(self, validated_data):
        return create_categoria(**validated_data)
