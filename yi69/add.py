from yi69.models import yi69
from django.http import JsonResponse
from users.models import UserProfile
from operation.models import operation
import time
def add_post(request):
    print("已捕获到请求")
    print(request.POST)
    print("准备取出关键数据")
    ret={}
    gotemail = (request.POST.get("email"))
    #首先进行用户权限验证
    useret = UserProfile.objects.get(email=gotemail)
    if(useret.level>=2):
        info = ["厂家","名称","型号","SN","数量","货柜号","备注","工程","资产标签"]
        cj = request.POST.get(info[0])
        name = request.POST.get(info[1])
        xinghao = request.POST.get(info[2])
        sn = request.POST.get(info[3])
        sl = request.POST.get(info[4])
        hgh = request.POST.get(info[5])
        bz = request.POST.get(info[6])
        gc = request.POST.get(info[7])
        zichanbiaoqian = request.POST.get(info[8])




        print("取出关键数据完毕,准备写入数据")
        n=yi69.objects.create(changjia=cj, mingcheng=name, xinghao=xinghao, sn=sn, \
                                           num=sl, place=hgh, beizhu=bz, gongcheng=gc, \
                                           zichanbiaoqian=zichanbiaoqian,status="入库申请中")
        print("写入数据完毕")
        print("写入输入ID",n.id)
        #操作记录存入后台
        operation.objects.create(name=useret.email, level=useret.level, op_type="入库申请", \
                                 op_res=True, op_item="169网")
        print("已记录到日志")
        ret["info"] = "已写入数据库 请核实"
        #1表示成功
        ret["type"] = 1
        ret["id"] = n.id

    else:
        print("用户权限不够")
        ret["info"] = "权限不够"
        ret["type"] = 0
    return JsonResponse(ret,safe=False)