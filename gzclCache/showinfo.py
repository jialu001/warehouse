from users.models import UserProfile
from .models import gzclcache
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = {}
    #get info

    gotId = request.GET.get("id")
    n=gzclcache.objects.get(id=gotId)
    fin_res["申请人"]= n.username
    fin_res["故障处理地点"]= n.chulididian
    fin_res["设备名称"]= n.itemName
    return JsonResponse(fin_res, safe=False)

