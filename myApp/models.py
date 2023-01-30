from django.db import models

class Post(models.Model):#数据库的数据取出后按照这个格式保存
     #models是django自带的 以下全函数是自带
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    # models.CASCADE 意思是删除时候是否伤处全部关联的objct 这里是 yes
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ["-data_added"]