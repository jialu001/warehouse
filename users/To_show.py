from django.shortcuts import render

##跳转至下一页面
def info_post1(request):

    return render(request, "UserInfo.html")