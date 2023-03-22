from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Register your models here.
admin.site.register(ContentType)
admin.site.register(Permission)
admin.site.register(Post)
admin.site.register(Comment)