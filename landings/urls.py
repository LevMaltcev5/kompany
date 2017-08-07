from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^about/$', views.about, name='about'),
    url(r'^registermail/$', views.regmail, name='regmail'),
    url(r'^registerphone/$', views.regphone, name='regphone'),
    url(r'^thx$', views.thx, name='thx'),
    url(r'^zimniki/$', views.zimniki),
    url(r'^perevozki/$', views.perevozki),
    url(r'^perevozka/$', views.perevoz),
]
