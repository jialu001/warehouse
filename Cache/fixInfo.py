from users.models import UserProfile
from .models import cache
from django.http import JsonResponse
from operation.models import operation
#tips : fix cache after committed
def fixInfo(request):
    fin_res = []
    gotID = request.GET.get("id")

    res = cache.objects.get(id=gotID)

    res.op_status="已审核"
    res.save()
    print("cache fixed")
    return JsonResponse(fin_res, safe=False)

