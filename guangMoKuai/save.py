from users.models import UserProfile
from .models import guangMoKuai
from django.http import JsonResponse
from operation.models import operation
def sh_Save(request):
    fin_res = []
    id = request.GET.get("id")
    res = guangMoKuai.objects.get(id=id)
    res.chengYuWang = res.chengYuWang + res.change
    res.change = 0
    res.status = "0"
    res.save()
    #print("光模块数据增加（删除）成功")
    return JsonResponse(fin_res, safe=False)

