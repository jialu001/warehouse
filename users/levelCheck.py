from .models import UserProfile
from django.http import JsonResponse
from operation.models import operation
def level_Check(request):
    gotemail = request.GET.get("email")
    ret = {}
    n = UserProfile.objects.get(email=gotemail);
    ret['level'] = n.level

    return JsonResponse(ret, safe=False)