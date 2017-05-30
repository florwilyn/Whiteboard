from django.conf.urls import url
from django.http import HttpResponse
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^add_group/$', views.add_group),
	url(r'^', include('whiteboard.urls')),
	# url(r'^', include('Project.urls'))

]