from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^trans/', views.transport, name='transport'),
    url(r'^product/(?P<transport_id>\w+)/$', views.evertrans, name='product'),
]
