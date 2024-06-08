from django.contrib import admin
from app_theater.models import *


class ProfileAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)

