"""
URL configuration for project_theater project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_theater.views import *
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-comment/', create_comment),
    path('create-discussion/', create_discussion),
    path('create-film/', create_film),
    path('create-menu-item/', create_menu_item),
    path('create-poll/', create_poll),
    path('create-post/', create_post),
    path('create-showtime/', create_showtime),
    path('create-user/', create_user),
    path('create-vote/', create_vote),
    path('delete-comment/', delete_comment),
    path('delete-discussion/', delete_discussion),
    path('delete-film/', delete_film),
    path('delete-menu-item/', delete_menu_item),
    path('delete-poll/', delete_poll),
    path('delete-post/', delete_post),
    path('delete-showtime/', delete_showtime),
    path('delete-showtime-day/', delete_showtimes_day),
    path('edit-film/', edit_film),
    path('edit-menu-item/', edit_menu_item),
    path('edit-post/', edit_post),
    path('get-comments/', get_comments),
    path('get-discussions/', get_discussions),
    path('get-films/', get_films),
    path('get-menu-items/', get_menu_items),
    path('get-polls/', get_polls),
    path('get-posts/', get_posts),
    path('get-showtimes/', get_showtimes),
    path('get-votes/', get_votes),
    path('profile/', get_profile),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('update-comment-likes/', update_comment_likes),
    path('update-likes/', update_likes),
    
]

if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)