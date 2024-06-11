from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser

from .models import *
from .serializers import *



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
def get_films(request):
   films = Film.objects.all().order_by('-created_at')
   films_serialized = FilmSerializer(films, many=True)
   return Response(films_serialized.data)


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
