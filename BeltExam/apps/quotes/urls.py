from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
	url(r'^register$', views.register, name='register'),
	url(r'^addQuote$', views.addQuote, name='addQuote'),
	url(r'^addFave/(?P<id>\d+)$', views.addFave, name='addFave'),
	url(r'^removeFave/(?P<id>\d+)$', views.removeFave, name='removeFave'),
	url(r'^showUserQuotes$', views.showUserQuotes, name='showUserQuotes'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout, name='logout'),
]

