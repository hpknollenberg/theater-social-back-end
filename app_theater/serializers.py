from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'is_admin']


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S EST")
    likes_count = serializers.IntegerField(source='likes.count')

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'content', 'image', 'likes_count', 'likes']

    
class FilmSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S EST")

    class Meta:
        model = Film
        fields = ['id', 'author', 'created_at', 'release_date', 'title', 'image']


class ChoiceSerializer(serializers.ModelSerializer):
    vote_count = serializers.IntegerField(source='votes.count')

    class Meta:
        model = Choice
        fields = ['id', 'name', 'vote_count']


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = ['id', 'name', 'choices']


class VoteSerializer(serializers.ModelSerializer):
    poll = PollSerializer(many=False, read_only=True)

    class Meta:
        model = Vote
        fields = ['id', 'profile', 'poll']


class DiscussionSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Discussion
        fields = ['id', 'author', 'name', 'description', 'image', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(many=False, read_only=True)
    discussion = DiscussionSerializer(many=False, read_only=True)
    likes_count = serializers.IntegerField(source='likes.count')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'discussion', 'content', 'likes_count', 'created_at', 'likes']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'price']


class SpecificTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificTime
        fields = ['id', 'hour_minute']


class ShowtimeSerializer(serializers.ModelSerializer):
    times = SpecificTimeSerializer(many=True)
    
    class Meta:
        model = Showtime
        fields = ['id', 'film', 'times', 'date']