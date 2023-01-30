from django.contrib import admin  # 系统自带 管理画面
from django.urls import path
from myApp.views import frontpage, post_detail  # 像导入包一样导入自己写的函数

urlpatterns = [
    # domin后面的所有所有网址 空字符串就是domin 根目录
    path('admin/', admin.site.urls),
    path("", frontpage),  # 根目录 调用view.py 的frontpage函数 #clent call server 1
    path("<slug:slug>/", post_detail, name="post_detail")
    # <slug:slug> 这种写法会默认为每个详细页面单独设定最终的url 比如 post-1 post-2
]

# path()函数三个参数   
# route: 字符串，表示URL的路径。它是一个正则表达式，可以包含占位符，如int: id，表示id为整数。
# view: 可调用对象，表示与URL路径关联的视图函数。当Django接收到请求后，会调用这个函数来处理请求并返回响应。
# name: 字符串，给视图函数命名。可以使用这个名字通过Django的urls模块进行反向URL解析。
# 所以path("<slug:slug>/", post_detail, name="post_detail")的意思是：
# 当请求的URL路径符合指定的正则表达式（slug: slug）时，调用视图函数post_detail处理请求，并给视图函数命名为post_detail。

# 第二参数函数的参数是django给的
