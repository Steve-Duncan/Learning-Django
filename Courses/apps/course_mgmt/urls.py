from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^show_comment/(?P<id>\d+)$', views.show_comment),
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment),
    url(r'^delete_comment/(?P<id>\d+)$', views.delete_comment)
]
