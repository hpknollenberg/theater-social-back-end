from django.contrib import admin
from app_theater.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class PollAdmin(admin.ModelAdmin):
    pass

class ChoiceAdmin(admin.ModelAdmin):
    pass

class VoteAdmin(admin.ModelAdmin):
    pass

class FilmAdmin(admin.ModelAdmin):
    pass

class DiscussionAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class MenuItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(MenuItem, MenuItemAdmin)