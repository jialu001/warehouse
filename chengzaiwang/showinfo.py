from users.models import UserProfile
from .models import chengzaiwang
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    sh_id =request.GET.get("id")
    e = chengzaiwang.objects.get(id=sh_id)
    ctx = {}
    ctx['分公司'] = e.fengongsi
    ctx['名称'] = e.name
    ctx['型号'] = e.xinghao
    ctx['类型'] = e.leixing
    ctx['sn'] = e.sn
    ctx['入库时间'] = e.rukushijian
    ctx['入库地点'] = e.rukudidian
    ctx['数量'] = e.num
    ctx['货位号'] = e.huoweihao
    ctx['订单号'] = e.dingdanhao
    ctx['调往地'] = e.diaowangdi
    ctx['调出时间'] = e.diaochushijian
    ctx['所属网络'] = e.suoshuwangluo
    ctx['备注'] = e.beizhu
    ctx['资产标签'] = e.zichanbiaoqian
    fin_res = ctx
    print(fin_res)
    return JsonResponse(fin_res, safe=False)

