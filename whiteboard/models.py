from __future__ import unicode_literals
from django.db import models
from user_profile.models import Users
import os

class Group(models.Model):
	group_name = models.CharField(max_length = 10)
	date_created = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(Users, null=True, default=None, on_delete=models.SET_NULL, related_name="owns")

	def __str__(self):
   		return self.group_name

class Member(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	member = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="is_a_member_of")

	def __str__(self):
   		return "{} ".format(self.id)

class Chat(models.Model):
	sender = models.ForeignKey(Users,null=True, default=None, on_delete=models.SET_NULL)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	content = models.CharField(max_length=200)
	date_sent = models.DateTimeField(auto_now_add=True)

	def __str__(self):
   		return "{} ".format(self.sender.user.id)

class Note(models.Model):
	note = models.CharField(max_length=100)
	owner = models.ForeignKey(Group,on_delete=models.CASCADE)
	new = models.BooleanField(default=True)