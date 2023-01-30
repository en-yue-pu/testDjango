from django.db import models

class Post(models.Model):#数据库的数据取出后按照这个格式保存
     #models是django自带的 以下全函数是自带
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)