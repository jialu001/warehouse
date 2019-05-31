from users.models import UserProfile
from .models import guangMoKuai
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    sh_id =request.GET.get("id")
    e = guangMoKuai.objects.get(id=sh_id)
    ctx = {}
    ctx['厂家']=e.changjia
    ctx['光模块型号'] =e.xinghao
    ctx['承载网数量']=e.chengZaiWang
    ctx['城域网数量'] = e.chengYuWang
    ctx['移交750数量'] = e.moveTo750
    ctx['即将入库数量'] =e.change
    fin_res = ctx
    print(fin_res)
    return JsonResponse(fin_res, safe=False)

