from django.conf.urls import include, url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.inicio, name='index'),
    url(r'^nuevo/$', views.nuevo, name='url_nuevo'),
    url(r'^ver/$', views.ver, name='url_ver'),
]
