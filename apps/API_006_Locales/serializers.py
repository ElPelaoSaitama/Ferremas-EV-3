from rest_framework import serializers
from .models import Local
from .services import crear_local

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

class LocalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'

    def create(self, validated_data):
        return crear_local(**validated_data)
