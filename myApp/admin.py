from django.contrib import admin
from .models import Post, Comment #同一个文件夹下的Post导入

admin.site.register(Post)
admin.site.register(Comment)