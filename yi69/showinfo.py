from users.models import UserProfile
from .models import yi69
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    fin_res = []
    show_type = request.GET.get("type")
    if(show_type=="fast"):
        gotEmail = request.GET.get("email")
        usersRet = UserProfile.objects.get(email=gotEmail)
        operation.objects.create(name=usersRet.email, level=usersRet.level, op_type="169网查询", \
                                 op_res=True, op_item="169")
        inp_get = request.GET.get("toolsname")
        res = yi69.objects.filter(mingcheng__icontains=inp_get)
        putFast(res, fin_res)
        print(fin_res)
    elif(show_type=="sh"):
        sh_id =request.GET.get("id")
        e = yi69.objects.get(id=sh_id)
        ctx = {}
        ctx['厂家'] = e.changjia
        ctx['设备名称'] = e.mingcheng
        ctx['设备型号'] = e.xinghao
        ctx['sn编码'] = e.sn
        ctx['数量'] = e.num
        ctx['存放地点'] = e.place
        ctx['备注信息'] = e.beizhu
        ctx['工程号'] = e.gongcheng
        ctx['资产标签'] = e.zichanbiaoqian
        fin_res = ctx
        print(fin_res)
    return JsonResponse(fin_res, safe=False)

def putFast(res,ret):
    # 将res 仅一部分json序列化 返回
    print("进入169查询模式")
    if (not res):
        print("查询内容为空")
        ret.append('null')
    for e in res:
        ctx = {}
        ctx['id'] = e.id
        ctx['changjia'] = e.changjia
        ctx['mingcheng'] = e.mingcheng
        ctx['xinghao'] = e.xinghao
        ctx['sn'] = e.sn
       # ctx['num'] = e.num
        ctx['place'] = e.place
       # ctx['beizhu'] = e.beizhu
        ctx['gongcheng'] = e.gongcheng
        #ctx['zichanbiaoqian'] = e.zichanbiaoqian
        ctx['状态'] = e.status
        ret.append(ctx)
    return ret