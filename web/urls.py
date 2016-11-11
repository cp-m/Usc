"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web import *
from web import views
from django.conf.urls import patterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.loop),
    url(r'^index.html',views.index),
    url(r'^cl.html',views.cl),
    url(r'^hztx.html',views.hztx),
    url(r'^ecduose.html', views.ecduose),
    url(r'^ecduoseht.html', views.ecduoseht),
    url(r'^ecduo.html', views.ecduo),
    url(r'^ecduoht.html', views.ecduoht),
    url(r'^tpsite.html', views.tpsite),
    url(R'^loop.html', views.loop),
    url(r'^accounts/login/$',include(admin.site.urls)),
]
#urlpatterns = patterns('web.views',
 #      (r'^mob/(\d*.html)/$', 'year_mob'),
 #             )

