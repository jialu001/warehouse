from guangMoKuai.models import guangMoKuai
from django.http import JsonResponse
from users.models import UserProfile
from operation.models import operation
import time
def add_post(request):
   # print("已捕获到请求")
    #print("准备取出关键数据")
    ret={}
    gotemail = (request.POST.get("email"))
    #首先进行用户权限验证
    useret = UserProfile.objects.get(email=gotemail)
    if(useret.level>=2):
        #cj 厂家
        gotCJ =request.POST.get("cj")
        gotXh=request.POST.get("xh")
        gotnum =request.POST.get("num")
       # print("cj",gotCJ)
        #print("xh",gotXh)
        #print("取出关键数据完毕,准备写入数据")
        try:
            n = guangMoKuai.objects.get(changjia=getCjChineseName(gotCJ),xinghao=gotXh)
            Num = gotnum.split(';')
            if(n.status=="0"):
                print("*************************:",Num[0])
                if (Num[0] =="0"):
                    n.change = int(Num[1])
                if (Num[0]=="1"):
                    n.change = -int(Num[1])
                print("#######################################:",Num[1])
                n.status ="1" ;
                n.save()
               # print("写入数据完毕")

                # 操作记录存入后台
                operation.objects.create(name=useret.email, level=useret.level, op_type="入库申请", \
                                         op_res=True, op_item="光模块")
                print("已记录到日志")
                ret["info"] = "已写入数据库 请核实"
                # 1表示成功
                ret["type"] = 1
                ret["id"] = n.id
            else:
                ret={}
                ret["type"] = -1
        except guangMoKuai.DoesNotExist:
            print("no  found")

        except guangMoKuai.MultipleObjectsReturned:
            print("multiple")



    else:
        print("用户权限不够")
        ret["info"] = "权限不够"
        ret["type"] = 0
    return JsonResponse(ret,safe=False)


def getCjChineseName(str):
    if(str=="sike"):
        return "思科"
    if(str == "huawei"):
        return "华为"
    if(str == "beier"):
        return "贝尔"
    if(str == "dipu"):
        return "迪普"
    if(str == "h3c"):
        return "H3C"