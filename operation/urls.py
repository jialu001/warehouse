from django.urls import path

from . import show

urlpatterns = [
    path('show', show.show, name='日志显示'),
]