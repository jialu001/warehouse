from users.models import UserProfile
from .models import ywktcache
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = {}
    #get info

    gotId = request.GET.get("id")
    n=ywktcache.objects.get(id=gotId)
    fin_res["申请人"]= n.username
    fin_res["调单号"]= n.diaodanHao
    fin_res["使用于设备"]= n.ToItemName
    fin_res["设备端口"] = n.ToItemSlot
    fin_res["出库设备名"] = n.itemName
    return JsonResponse(fin_res, safe=False)

