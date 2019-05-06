from django.shortcuts import render

##数据库查询
def to_index(request):

    return render(request, "index.html")