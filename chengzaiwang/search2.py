from chengzaiwang.models import chengzaiwang
from django.http import JsonResponse
from operation.models import operation
from users.models import UserProfile
##数据库查询



def search_post(request):

    ret = []
    gotemail = request.GET.get("email")
    useret = UserProfile.objects.get(email=gotemail)

    #print("关键字为",request.GET.get("toolsname"))
    try:
        print(request.GET.get("type"))
        if(request.GET.get("type")=="fast"):
            if (sql_detect(request.GET.get("toolsname"))):
             #   print("捕获到异常，即将返回前端")
                raise ValueError('SQL detected')


            res = chengzaiwang.objects.filter(name__icontains=(request.GET.get("toolsname")))
                   #将res序列化 放到ret里面
            ret=putFast(res,ret)
        elif(request.GET.get("type")=="nor"):
         #   print("进入详细查询模式")
            idset = ["fenggongsi", "name", "xinghao", "leixing", "sn", "rukushijian", "rukudidian",
                     "shuliang", "huoweihao", "suoshuwangluo", "zichanbiaoqian", "beizhu"];
            res = chengzaiwang.objects.all()
            for x in idset:
                str = x + "ischecked"
                if(request.GET.get(str)=="true"):
                    res=indexSearch(x,res,request.GET.get(x))
            putNor(res, ret)
        print(gotemail)
        print(ret)
        operation.objects.create(name=useret.email,level=useret.level,op_type="搜索",\
                                     op_res=True,op_item="item")



    except Exception:
        ctx = ['error']
     #   print("发现异常并返回前端",ctx)
        ret = ctx


    return JsonResponse(ret,safe=False)

def putFast(res,ret):
    # 将res 仅一部分json序列化 返回
 #   print("进入快捷查询模式")

    if (not res):
        #如果目标集为空，则返回结果集置为 null
        ret = ['null']
    else:
        for e in res:
            ctx = {}
            ctx['name'] = e.name
            ctx['xinghao'] = e.xinghao
            ctx['sn'] = e.sn
            ctx['huoweihao'] = e.huoweihao
            ctx['status'] = e.status
            ctx['id'] = e.id
            ctx['beizhu'] = e.beizhu
            ret.append(ctx)

    return ret
def putNor(res,ret):
    #将res json序列化 返回
   # print("进入正常查询模式")
    if (not res):
        ret = ['null']
    for e in res:
        ctx = {}
        ctx['fengongsi'] = e.fengongsi
        ctx['name'] = e.name
        ctx['xinghao'] = e.xinghao
        ctx['leixing'] = e.leixing
        ctx['sn'] = e.sn
        ctx['rukushijian'] = e.rukushijian
        ctx['rukudidian'] = e.rukudidian
        ctx['num'] = e.num
        ctx['huoweihao'] = e.huoweihao
        ctx['dingdanhao'] = e.dingdanhao
        ctx['diaowangdi'] = e.diaowangdi
        ctx['diaochushijian'] = e.diaochushijian
        ctx['suoshuwangluo'] = e.suoshuwangluo
        ctx['beizhu'] = e.beizhu
        ctx['zichanbiaoqian'] = e.zichanbiaoqian
        ret.append(ctx)
    return ret

def indexSearch(str,ret,value):
    # str 用于确定搜索方法 ，value是关键字

    idset = ["fengongsi", "name", "xinghao", "leixing", "sn", "rukushijian", "rukudidian",
             "shuliang", "huoweihao", "suoshuwangluo", "zichanbiaoqian", "beizhu"];
    if(str=="fenggongsi"):
        ret = ret.filter(fengongsi__icontains=value)
    elif(str=="name"):
     #   print("进入name查询")
        ret = ret.filter(name__icontains=value)
    elif (str == "xinghao"):
       # print("进入value查询")
       # print("此时value为：",value)
        ret = ret.filter(xinghao__icontains=value)
    return ret
#定义一个判断字符串是否为数字的函数
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False

#sql注入判断
def sql_detect(s):
    s = s.lower()
    #print("待检测字符已经转为小写", s)
    sql = ["delete","create","insert","update","drop","alter","grant","deny"]
    result = False
    for key in sql:
        if(compare(s,key)):
            result = True

    print("SQL关键检测结果为",result)
    return result

#字符串比较
def compare(fat,son):
    result= False
    length = 0
    i=0
    ist=0
    j=0



    while i < (len(fat)):
       # print("外圈循环",i)
        while j<len(son):
            #字符匹配成功
            if(fat[i] == son[j]):
                if(j==0):
                    ist = i+1
                   # print("检测到疑似值,已保存初始位置",ist)
                length=length+1
                j=j+1
                break
            #不成功
            else:
                if(length>0):

                   # print("此时已匹配长度为",length,"外圈长度",i)
                    i = ist
                    #print("内圈置为0")
                    length = 0
                    j=0


                break
        if(length==len(son)):
            result=True
           # print("检测到目标值")
            break
        else:
            i = i + 1


   # print("跳出循环,并输出关键字:",son,"的匹配结果",result)

    return result