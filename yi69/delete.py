from .models import yi69
from django.http import JsonResponse
def cKdelete(request):
    fin_res = []
    id = request.GET.get("id")
    yi69.objects.get(id=id).delete()
    print("删除成功")
    return JsonResponse(fin_res, safe=False)