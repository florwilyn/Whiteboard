from django.conf.urls import url
from django.http import HttpResponse
from . import views

urlpatterns = [
	url(r'^add_group/$', views.add_group),
]