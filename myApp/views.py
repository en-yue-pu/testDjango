from django.shortcuts import render
from .models import Post

def frontpage(request): #clent call server 2
    posts = Post.objects.all()#取得Post所有数据 保存成POST格式
    return render(request, "htmls/frontpage.html", {"posts": posts})#追加第三参数
    #path默认是 templates文件夹下 open一个html文件
