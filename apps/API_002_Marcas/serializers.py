from rest_framework import serializers
from .models import Marca

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre')

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value
