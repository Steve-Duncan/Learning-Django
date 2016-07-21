from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_money$', views.process_money),
    url(r'^show_money$', views.show_money),
    url(r'^reset$', views.index)
]
