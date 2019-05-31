from django.urls import path
from . import showinfo
from . import allinfo
from . import add
from . import sheninfo
from . import save
urlpatterns = [
    path('info',showinfo.showInfo,name='showinfo'),
    path('allinfo',allinfo.showInfo,name='get all info'),
    path('add', add.add_post, name='add info'),
    path('shinfo',sheninfo.showInfo,name='sh'),
    path('save', save.sh_Save, name='save'),
]