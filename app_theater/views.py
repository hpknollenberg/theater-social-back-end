from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
import simplejson as json

from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
   Comment.objects.create(
      author = Profile.objects.get(id=request.data['author']),
      content = request.data['content'],
      discussion = Discussion.objects.get(id=request.data['discussion']),
   )
   return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_discussion(request):
   if request.data['is_admin'] == 'true':
      Discussion.objects.create(
         author = Profile.objects.get(id=request.data['author']),
         name = request.data['name'],
         description = request.data['description'],
         image = request.data['image']
      )
      return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_film(request):
   if request.data['is_admin'] == "true":
      Film.objects.create(
         author = Profile.objects.get(id=request.data['author']),
         release_date = request.data['release_date'],
         title = request.data['title'],
         image = request.data['image']
      )
      return Response()
   

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_menu_item(request):
   if request.data['is_admin'] == 'true':
      MenuItem.objects.create(
         name = request.data['name'],
         category = request.data['category'],
         price = request.data['price']
      )
      return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_poll(request):
   if request.data['is_admin'] == "true":
      Poll.objects.create(
         name = request.data['title'],
         id = request.data['id']
      )
      poll = Poll.objects.get(pk = request.data['id'])
      choices = json.loads(request.data['choices'])
      for choice in choices:
         Choice.objects.create(
            name=choice,
            poll=poll
            )
      return Response()



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):
   if request.data['is_admin'] == "true":
      Post.objects.create(
         author = Profile.objects.get(id=request.data['author']),
         content = request.data['content'],
         image = request.data['image']
      )
      return Response()


@api_view(['POST'])
@permission_classes([])
def create_user(request):
  user = User.objects.create(
    username = request.data['username'],
  )
  user.set_password(request.data['password'])
  user.save()
  profile = Profile.objects.create(
   user = user,
   first_name = request.data['first_name'],
   last_name = request.data['last_name']
  )
  profile.save()
  profile_serialized = ProfileSerializer(profile)
  return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([])
def create_vote(request):
   if not Vote.objects.filter(profile=request.data['profile'], poll=request.data['poll']).exists():
      vote = Vote.objects.create(
         profile = Profile.objects.get(id=request.data['profile']),
         poll = Poll.objects.get(id=request.data['poll']),
         choice = Choice.objects.get(id=request.data['choice'])
      )
      vote.save()
      vote_serialized = VoteSerializer(vote)
      return Response(vote_serialized.data)
   

@api_view(['DELETE'])
@permission_classes([])
def delete_comment(request):
   comment = Comment.objects.get(id=request.data['comment'])
   comment.delete()
   return Response()
      

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_discussion(request):
   if request.data['is_admin'] == True:
      discussion = Discussion.objects.get(id=request.data['discussion'])
      discussion.delete()
      return Response()

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def delete_film(request):
   if request.data['is_admin'] == 'true':
      film = Film.objects.get(id=request.data['film'])
      film.delete()
      return Response()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_menu_item(request):
   if request.data['is_admin'] == True:
      menu_item = MenuItem.objects.get(id=request.data['menu_item'])
      menu_item.delete()
      return Response()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_poll(request):
   if request.data['is_admin'] == True:
      poll = Poll.objects.get(id=request.data['poll'])
      poll.delete()
      return Response()


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def delete_post(request):
  if request.data['is_admin'] == 'true':
    post = Post.objects.get(id=request.data['post'])
    post.delete()
    return Response()


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def edit_film(request):
   if request.data['is_admin'] == 'true':
      film = Film.objects.get(id=request.data['film'])
      film.title = request.data['title']
      film.release_date = request.data['release_date']
      film.save(update_fields=['title', 'release_date'])
      if request.data['image'] != "":
         film.image = request.data['image']
         film.save(update_fields=['image'])
      edit_film_serialized = FilmSerializer(film)
      return Response(edit_film_serialized.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def edit_post(request):
   if request.data['is_admin'] == 'true':
      post = Post.objects.get(id=request.data['post'])
      post.content = request.data['content']
      post.save(update_fields=['content'])
      if request.data['image'] != "":
        post.image = request.data['image']
        post.save(update_fields=['image'])
      edit_post_serialized = PostSerializer(post)
      return Response(edit_post_serialized.data)
   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request):
   comments = Comment.objects.all().order_by('-created_at')
   comments_serialized = CommentSerializer(comments, many=True)
   return Response(comments_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_discussions(request):
   discussions = Discussion.objects.all().order_by('-created_at')
   discussions_serialized = DiscussionSerializer(discussions, many=True)
   return Response(discussions_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_films(request):
   films = Film.objects.all().order_by('-created_at')
   films_serialized = FilmSerializer(films, many=True)
   return Response(films_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_menu_items(request):
   menu_items = MenuItem.objects.all().order_by('price')
   menu_items_serialized = MenuItemSerializer(menu_items, many=True)
   return Response(menu_items_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_polls(request):
   polls = Poll.objects.all()
   polls_serialized = PollSerializer(polls, many=True)
   return Response(polls_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    posts_serialized = PostSerializer(posts, many=True)
    return Response(posts_serialized.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_votes(request):
   user = request.user
   profile = user.profile
   votes = Vote.objects.filter(profile=profile)
   votes_serialized = VoteSerializer(votes, many=True)
   return Response(votes_serialized.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_comment_likes(request):
   user = request.user
   profile = user.profile
   profile_comment_likes = profile.comment_likes
   comment = Comment.objects.get(id=request.data['comment'])
   if comment.likes.filter(id=profile.id).exists():
      profile_comment_likes.remove(comment)
   else:
      profile_comment_likes.add(comment)
   comment_likes_serialized = CommentSerializer(profile_comment_likes, many=True)
   return Response(comment_likes_serialized.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_likes(request):
   user = request.user
   profile = user.profile
   profile_likes = profile.likes
   post = Post.objects.get(id=request.data['post'])
   if post.likes.filter(id=profile.id).exists():
      profile_likes.remove(post)
   else:
      profile_likes.add(post)
   likes_serialized = PostSerializer(profile_likes, many=True)
   return Response(likes_serialized.data)


