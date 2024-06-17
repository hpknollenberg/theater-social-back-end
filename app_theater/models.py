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

    def __str__(self):
        return self.content

class Film(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name="author_film")
    created_at = models.DateTimeField(auto_now_add=True)
    release_date = models.TextField()
    title = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Poll(models.Model):
    name = models.TextField()
    id = models.TextField(primary_key=True)

    def __str__(self):
        return self.name
    

class Choice(models.Model):
    name = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="choices", null=True, blank=True)

    def __str__(self):
        return self.name
    

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="votes", null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes", null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="votes", null=True, blank=True)

    def __str__(self):
        return self.profile.user.username


class Discussion(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="discussion", null=True)
    name = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="comment", null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="discussion_comments", null=True)
    likes = models.ManyToManyField(Profile, related_name="comment_likes")

    def __str__(self):
        return self.content
    

class MenuItem(models.Model):
    name = models.TextField()
    category = models.TextField()
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name