from django.urls import path
from . import showinfo
from . import delete
from . import save
urlpatterns = [
    path('info',showinfo.showInfo,name='showinfo'),
    #path('add', add.add_post, name='add'),
    path('save', save.sh_Save, name='save'),
    path('delete', delete.cKdelete, name='de'),
]