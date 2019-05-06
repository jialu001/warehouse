from django.http import JsonResponse
def query(request):
    r=request.GET.get("toolsname")
    name_dict="123"
    return JsonResponse(name_dict,safe=False)