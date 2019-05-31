from django.urls import path
from . import add
from . import showinfo
urlpatterns = [
    path('add', add.addDeal, name='add deal'),
    path('info', showinfo.showInfo, name='showinfo'),
]