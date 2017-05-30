from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import os

class Users(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	date_joined = models.DateTimeField(auto_now_add=True)
	prof_pic = models.ImageField(upload_to = './storage/', default = 'storage/default-avatar.png')

	def __str__(self):
   		return "{} ".format(self.id) + self.first_name
