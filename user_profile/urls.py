from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^add_group/$', views.add_group),
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^signout/$', views.signout, name='signout'),
	url(r'^signup/$', views.signup, name='signup'),
]