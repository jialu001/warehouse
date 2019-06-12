"""warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from extra_apps import To_main,to_log,to_contact,To_newIndex
from django.conf.urls import url
from django.views.static import serve
from warehouse.settings import MEDIA_ROOT
from chengzaiwang import To_search,testajax,To_dh,add
from chengzaiwang import search2

from users.To_show import info_post1
urlpatterns = [
    path('',to_log.to_des),  # new
    path('log',to_log.to_des),  # new
    path('index.html', To_main.to_index),  # new
    path('new', To_newIndex.to_index),  # 新主页测试
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('search.html', To_search.search_post1),
    #search里面ajax 的请求URL
    path('search-post', search2.search_post),
    #dh.js里面ajax 的请求URL
    path('add', add.add_post),
    #进去dh页面
    path('dh', To_dh.dh_post1),

    path('query/', testajax.query),
    #将user里面的url加入
    path('users/', include('users.urls')),
    #将op里面的url加入
    path('op/', include('operation.urls')),
    #将gmk里面的url加入
    path('gmk/', include('guangMoKuai.urls')),
    # 将169里面的url加入
    path('169/', include('yi69.urls')),
    # 将cache里面的url加入
    path('cache/', include('Cache.urls')),
    # 将czw里面的url加入
    path('czw/', include('chengzaiwang.urls')),
    # 将gcck里面的url加入
    path('gcck/', include('gcckCache.urls')),
    # 将ywkt里面的url加入
    path('ywkt/', include('ywktCache.urls')),
    # 将gzcl里面的url加入
    path('gzcl/', include('gzclCache.urls')),
    path('showinfo', info_post1, name='用户页面跳转'),
    path('contactUs', to_contact.to_Con, name='用户页面跳转'),
]
