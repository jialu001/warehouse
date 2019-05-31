from chengzaiwang.models import chengzaiwang
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
        info = ["fenggongsi", "name", "xinghao", "leixing", "sn", "dingdanhao", "rukudidian",
                "shuliang", "huoweihao", "suoshuwangluo", "zichanbiaoqian", "beizhu"];
        fenggongsi = request.POST.get(info[0])
        name = request.POST.get(info[1])
        xinghao = request.POST.get(info[2])
        leixing = request.POST.get(info[3])
        sn = request.POST.get(info[4])
        dingdanhao = request.POST.get(info[5])
        rukudidian = request.POST.get(info[6])
        shuliang = request.POST.get(info[7])
        huoweihao = request.POST.get(info[8])
        suoshuwangluo = request.POST.get(info[9])
        zichanbiaoqian = request.POST.get(info[10])
        beizhu = request.POST.get(info[11])
        rukushijian =(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



        print("取出关键数据完毕,准备写入数据")
        n=chengzaiwang.objects.create(fengongsi=fenggongsi, leixing=leixing, xinghao=xinghao, name=name, \
                                           sn=sn, rukudidian=rukudidian, dingdanhao=dingdanhao, num=shuliang, \
                                           huoweihao=huoweihao, suoshuwangluo=suoshuwangluo,
                                           zichanbiaoqian=zichanbiaoqian, beizhu=beizhu,rukushijian=rukushijian,status="入库申请中")
        print("写入数据完毕")
        #操作记录存入后台
        operation.objects.create(name=useret.email, level=useret.level, op_type="入库", \
                                 op_res=True, op_item="item")
        ret["info"] = "已写入数据库 请核实"
        #1表示成功
        ret["type"] = 1
        ret['id'] = n.id
    else:
        print("用户权限不够")
        ret["info"] = "权限不够"
        ret["type"] = 0
    return JsonResponse(ret,safe=False)