from django.db import models
from django.contrib.auth.models import User

def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'avatars/user_{instance.user.id}.{ext}'

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, default='avatars/default.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"