from django.shortcuts import render

##跳转到search 页面
def search_post1(request):

    return render(request, "search.html")