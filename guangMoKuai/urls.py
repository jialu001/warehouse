from django.urls import path
from . import showinfo
from . import allinfo

urlpatterns = [
    path('info',showinfo.showInfo,name='showinfo'),
    path('allinfo',allinfo.showInfo,name='get all info'),
]