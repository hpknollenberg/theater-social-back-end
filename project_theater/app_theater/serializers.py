from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name']


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S EST")
    likes_count = serializers.IntegerField(source='likes.count')

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'content', 'image', 'likes_count']