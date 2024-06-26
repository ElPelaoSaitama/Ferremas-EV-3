from django.contrib.auth.models import User

def create_user(username, password): 
    user = User.objects.create(username=username)
    user.set_password(password)
    user.save()
    return user

def get_user(user_id):
    return User.objects.get(id=user_id)

def update_user(user, username=None):
    if not User.objects.filter(pk=user.pk).exists():
        raise User.DoesNotExist("User does not exist.")
    
    if username:
        user.username = username
    
    user.save()
    return user

def delete_user(user):
    if not User.objects.filter(pk=user.pk).exists():
        raise User.DoesNotExist("User does not exist.")
    
    user.delete()
