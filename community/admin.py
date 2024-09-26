from django.contrib import admin

# Register your models here.

from .models import Post, Star


admin.site.register(Post)
admin.site.register(Star)