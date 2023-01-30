from django.shortcuts import render, redirect
from .models import Post
# view函数  这个页面一杯打开时候调用的函数 request是客户断访问请求 的实例


def frontpage(request):  # clent call server 2
    posts = Post.objects.all()  # 取得Post所有数据 保存成POST格式
    return render(request, "htmls/frontpage.html", {"posts": posts})  # 追加第三参数
    # path默认是 templates文件夹下 open一个html文件


def post_detail(request, slug):# slug格式是自己在 管理画面 填写的  要一致
    #slug就是url最后的一段 
    post = Post.objects.get(slug=slug)
    return render(request, "htmls/post_detail.html", {"post": post})
