from django.shortcuts import render

def frontpage(request): #clent call server 2
    return render(request, "htmls/frontpage.html")
    #path默认是 templates文件夹下 open一个html文件