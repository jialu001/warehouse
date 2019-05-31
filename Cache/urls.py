from django.urls import path
from . import Up
from . import showinfo
from . import fixInfo
urlpatterns = [
    path('up',Up.upDeal,name='up deal'),
    path('info',showinfo.showInfo,name='showinfo'),
    path('fix', fixInfo.fixInfo, name='fix'),
]