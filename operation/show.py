from django.http import JsonResponse
from .models import operation

def show(request):
    ret = []
    res = operation.objects.all()
    getALL(res,ret)
    print("读取完毕，即将返回前端")
    return JsonResponse(ret,safe=False)

def getALL(res,ret):
    # 将res 仅一部分json序列化 返回
    print("读取所有系统日志")
    if (not res):
        ret = ['null']
    for e in res:
        ctx = {}
        ctx['email'] = e.name
        ctx['level'] = e.level
        ctx['op_date'] = e.op_date
        ctx['op_type'] = e.op_type

        ret.append(ctx)
    return ret