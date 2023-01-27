from django.contrib import admin
from django.urls import path
from myApp.views import frontpage #像导入包一样导入自己写的函数

urlpatterns = [
    # domin后面的所有所有网址 空字符串就是domin 根目录
    path('admin/', admin.site.urls),
    path("", frontpage),#根目录 调用view.py 的frontpage函数 #clent call server 1 


]
