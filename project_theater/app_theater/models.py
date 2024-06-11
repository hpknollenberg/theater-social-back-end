from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="author_post")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    likes = models.ManyToManyField(Profile, related_name="likes")

class Film(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="author_film")
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.TextField()
    title = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)