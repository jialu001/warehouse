from .models import UserProfile
from django.http import JsonResponse
from operation.models import operation
def showInfo(request):
    ret ={}
    gotEmail = request.GET.get("email")
    usersRet = UserProfile.objects.get(email=gotEmail)
    ret["id"] = usersRet.id
    ret["姓名"] = usersRet.name
    ret["权限等级"] = usersRet.level
    ret["密码"] = usersRet.password
    ret["电话"] = usersRet.mobile
    ret["邮箱"] = usersRet.email
    ret["type"] = 1
    ret["info"] = "获取信息成功"
    operation.objects.create(name=usersRet.email, level=usersRet.level, op_type="显示个人信息", \
                             op_res=True, op_item="用户")
    return JsonResponse(ret, safe=False)