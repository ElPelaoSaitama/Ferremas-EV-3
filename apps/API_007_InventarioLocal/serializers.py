from rest_framework import serializers
from apps.API_007_InventarioLocal.models import InventarioLocal

class InventarioLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioLocal
        fields = ('local', 'productos', 'stock')