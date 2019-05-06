from .models import UserProfile
from django.http import JsonResponse
from operation.models import operation
def user_Check(request):
    gotemail = request.POST.get("email")
    ret = {}
    try:
        eml = UserProfile.objects.get(email=gotemail)

        if(eml.password != request.POST.get("password")):
            ret["type"] = "f"
            ret["info"] = "该email正确，但是密码输入错误"
        else:
            ret["type"] = "t"
            ret["info"] = "欢迎"
            ret["email"] = gotemail
            operation.objects.create(name=gotemail,level=eml.level,op_type="登录",\
                                     op_res=True,op_item="user")

        print(ret)
    except Exception:
        print("发生异常")
        ret["type"] = "f"
        ret["info"] = "多半你输入的email有问题"

    return JsonResponse(ret, safe=False)