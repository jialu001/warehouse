from users.models import UserProfile
#from .models import gcckcache
from django.http import JsonResponse
from chengzaiwang.models import chengzaiwang
from .models import ywktcache
from yi69.models import yi69
from operation.models import operation
#上传到申请库
def addDeal(request):

    fin_res = {}
    print("已捕获到业务开通出库申请")
    diaodanhao = request.GET.get("调单号")
    shebeiming = request.GET.get("设备名")
    duankouhao = request.GET.get("端口号")
    itemname = request.GET.get("itn")
    item_id = request.GET.get("itid")
    user_email = request.GET.get("email")
    gotU=UserProfile.objects.get(email=user_email)
    user_name = gotU.name
    net_type= request.GET.get("netT")

    #n=gcckcache.objects.create(gongCnum=GCid,username=user_name,itemName=itemname,itemId=item_id,itemNet=net_type)
    # 0 -czw
    if(net_type=="0"):
        n = ywktcache.objects.create(diaodanHao=diaodanhao,itemName=itemname,ToItemSlot=duankouhao, \
                                     username=user_name,ToItemName=shebeiming,itemId=item_id,\
                                     itemNet="承载网")

        c = chengzaiwang.objects.get(id=item_id)
        c.status = "出库申请中"
        c.save()
    if (net_type == "2"):
        n = ywktcache.objects.create(diaodanHao=diaodanhao, itemName=itemname, ToItemSlot=duankouhao, \
                                     username=user_name, ToItemName=shebeiming, itemId=item_id, \
                                     itemNet="169网")
        c = yi69.objects.get(id=item_id)
        c.status = "出库申请中"
        c.save()
    fin_res["id"]=n.id
    fin_res["item"]=itemname
    fin_res["info"]="工程出库申请成功，等待审核中"



    return JsonResponse(fin_res, safe=False)

