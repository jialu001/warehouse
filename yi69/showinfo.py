from users.models import UserProfile
from .models import yi69
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = []

    gotEmail = request.GET.get("email")
    usersRet = UserProfile.objects.get(email=gotEmail)

    operation.objects.create(name=usersRet.email, level=usersRet.level, op_type="169网查询", \
                             op_res=True, op_item="169")
    inp_get = request.GET.get("toolsname")
    res = yi69.objects.filter(mingcheng__icontains=inp_get)
    putFast(res, fin_res)
    return JsonResponse(fin_res, safe=False)

def putFast(res,ret):
    # 将res 仅一部分json序列化 返回
    print("进入169查询模式")
    if (not res):
        ret = ['null']
    for e in res:
        ctx = {}
        ctx['id'] = e.id
        ctx['changjia'] = e.changjia
        ctx['mingcheng'] = e.mingcheng
        ctx['xinghao'] = e.xinghao
        ctx['sn'] = e.sn
        ctx['num'] = e.num
        ctx['place'] = e.place
        ctx['beizhu'] = e.beizhu
        ctx['gongcheng'] = e.gongcheng
        ctx['zichanbiaoqian'] = e.zichanbiaoqian

        ret.append(ctx)
    return ret