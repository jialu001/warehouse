from users.models import UserProfile
from .models import cache
from django.http import JsonResponse
from operation.models import operation
#从库读取入库申请的
def showInfo(request):
    fin_res = []
    gotEmail = request.GET.get("email")
    usersRet = UserProfile.objects.get(email=gotEmail)
    operation.objects.create(name=usersRet.email, level=usersRet.level, op_type="申请处理", \
                             op_res=True, op_item="出入库申请")
    res = cache.objects.filter(op_status__icontains="申请")

    putFast(res, fin_res)
    print(fin_res)
    return JsonResponse(fin_res, safe=False)

def putFast(res,ret):
    # 将res 仅一部分json序列化 返回
    print("即将进入审核页面")
    if (not res):
        ret = ['null']
    for e in res:
        ctx = {}
        ctx['reason'] = e.op_reason
        ctx['id']=e.id
        ctx['email'] = e.op_user_name
        ctx['type'] = e.op_type
        ctx['item'] = e.op_item
        ctx['item_id'] = e.op_item_id
        ctx['time'] = e.op_time
        ret.append(ctx)
    return ret