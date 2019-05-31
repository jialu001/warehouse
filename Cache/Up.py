from users.models import UserProfile
from .models import cache
from django.http import JsonResponse
from operation.models import operation
#上传到申请库
def upDeal(request):

    fin_res = {}
    item = request.GET.get("item")
    item_id = request.GET.get("id")
    user_email = request.GET.get("email")
    op_type= request.GET.get("type")
    op_reason = request.GET.get("reason")
    if(op_type=="ruku"):
        n=cache.objects.create(op_user_name=user_email,op_type=op_type,op_item=item, \
                           op_item_id=item_id,op_status="入库申请",op_reason=op_reason)
    if(op_type=="出库"):
        n = cache.objects.create(op_user_name=user_email, op_type=op_type, op_item=item, \
                                 op_item_id=item_id, op_status="出库申请", op_reason=op_reason)
    print("已捕获到申请")


    fin_res["info"]="申请成功，等待审核中"



    return JsonResponse(fin_res, safe=False)

