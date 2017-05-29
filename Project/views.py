from django.shortcuts import render, redirect
from whiteboard.models import Chat
from whiteboard.models import Group
from whiteboard.models import Member
from user_profile.models import Users
from whiteboard.models import Note

def index(request, group_id):
	#get user credentials
	user_id = request.user.id
	user = Users.objects.get(user__id=user_id)
	group = Member.objects.filter(member__pk=user.pk)

	#get group and members
	group_name = Group.objects.get(id=group_id)
	members = Member.objects.filter(group__id=group_id)

	#get chat content
	group_chat = Chat.objects.filter(group__id=group_id)

	#notes
	notes = Note.objects.filter(owner__id=group_id)
	
	return render(request, 'index.html', {'group_chat': group_chat, 'user': user, 'group': group, 'group_name': group_name, 'members': members, 'notes': notes, 'group_id': group_id})

def profile(request):
	user_id = request.user.id
	user = Users.objects.get(user__id=user_id)
	group = Member.objects.filter(member__pk=user.pk)
	print(group.query)
	return render(request, 'profile.html', { 'user': user, 'group': group})

def edit_profile(request):
	user_id = request.user.id
	user = Users.objects.get(user__id=user_id)
	group = Member.objects.filter(member__pk=user.pk)

	return render(request, 'edit_profile.html', {'user': user, 'group': group})