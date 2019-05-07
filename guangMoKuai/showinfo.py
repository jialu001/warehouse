from users.models import UserProfile
from .models import guangMoKuai
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = []
    ret ={}
    gotEmail = request.GET.get("email")
    usersRet = UserProfile.objects.get(email=gotEmail)

    operation.objects.create(name=usersRet.email, level=usersRet.level, op_type="光模块查询", \
                             op_res=True, op_item="光模块")
    inp_get = request.GET.get("toolsname")
    res = guangMoKuai.objects.filter(xinghao__icontains=inp_get)
    putFast(res, fin_res)
    return JsonResponse(fin_res, safe=False)

def putFast(res,ret):
    # 将res 仅一部分json序列化 返回
    print("进入光模块查询模式")
    if (not res):
        ret = ['null']
    for e in res:
        ctx = {}
        ctx['id'] = e.id
        ctx['changjia'] = e.changjia
        ctx['xinghao'] = e.xinghao



        ret.append(ctx)
    return ret