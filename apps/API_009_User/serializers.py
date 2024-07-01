from django.contrib.auth import get_user_model
from rest_framework import serializers
from .services import create_user, get_user, update_user, delete_user

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = { 'password': { 'write_only': True }}

        def create(self, validated_data):
            return create_user(**validated_data)



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'