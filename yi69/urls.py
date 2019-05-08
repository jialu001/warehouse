from django.urls import path
from . import showinfo

urlpatterns = [
    path('info',showinfo.showInfo,name='showinfo'),

]