from django.urls import path
from . import login_check,showinfo

urlpatterns = [
    path('check', login_check.user_Check, name='登录验证'),
    path('info',showinfo.showInfo,name='showinfo'),

]