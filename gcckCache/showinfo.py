from users.models import UserProfile
from .models import gcckcache
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = {}
    #get info

    gotId = request.GET.get("id")
    n=gcckcache.objects.get(id=gotId)
    fin_res["申请人"]= n.username
    fin_res["工程号"]= n.gongCnum
    fin_res["设备名称"]= n.itemName
    return JsonResponse(fin_res, safe=False)

