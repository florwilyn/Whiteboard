from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	#url(r'^$', views.index),
	url(r'^post/$', views.Post),
	    url(r'^add_member/$', views.add_member),
    url(r'^add_note/$', views.add_note),
    url(r'^chat/(?P<group_id>\d+)/$', views.chat, name='chat'),
]