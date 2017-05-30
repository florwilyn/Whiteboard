from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	#url(r'^$', views.index),
	url(r'^post/$', views.Post, name='post'),
	url(r'^add_member/$', views.add_member),
	url(r'^delete_note/$', views.delete_note, name='delete'),
    url(r'^add_note/$', views.add_note),
    url(r'^chat/(?P<group_id>\d+)/$', views.chat, name='chat'),
    url(r'^notes/(?P<group_id>\d+)/$', views.notes, name='chat'),
     url(r'^members/(?P<group_id>\d+)/$', views.members, name='members'),
]