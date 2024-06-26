from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UserRegistrationSerializer, UserUpdateSerializer
from .services import delete_user, get_user, update_user


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_object(self):
        return get_user(self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return self.serializer_class
    
    def perform_update(self, serializer):
        update_user(serializer.instance, **serializer.validated_data)
    
    def perform_destroy(self, instance):
        delete_user(instance)
        

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer