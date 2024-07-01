from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def create_user(username, password): 
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return user

def get_user(user_id):
    return User.objects.get(id=user_id)

def update_user(user_id, **kwargs):
    try:
        user = User.objects.get(id=user_id)
        updated = False

        for key, value in kwargs.items():
            if getattr(user, key) != value:
                setattr(user, key, value)
                updated = True

        if not updated:
            raise ValueError("No se detectaron cambios en el usuario.")

        user.save()
        return user

    except User.DoesNotExist:
        raise ObjectDoesNotExist(f"El usuario con ID {user_id} no existe en la base de datos.")

def delete_user(user):
    if not User.objects.filter(pk=user.pk).exists():
        raise User.DoesNotExist("User does not exist.")
    
    user.delete()

def dell_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return user
    except User.DoesNotExist:
        raise ObjectDoesNotExist(f"El usuario con ID {user_id} no existe en la base de datos.")