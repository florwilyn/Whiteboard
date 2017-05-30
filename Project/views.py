from django.shortcuts import render, redirect
from whiteboard.models import Chat
from whiteboard.models import Group
from whiteboard.models import Member
from user_profile.models import Users
from whiteboard.models import Note
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_list_or_404, get_object_or_404

def index(request, group_id):
	if request.user.is_authenticated():

		#get user credentials
		user_id = request.user.id

		user = Users.objects.get(user__id=user_id)


		# is_member_of = Member.objects.get_object_or_404()
		is_member_of = get_list_or_404(Member, member__pk=user.id, group__id=group_id)

		group = Member.objects.filter(member__pk=user.pk)

		#get group and members
		group_name = Group.objects.get(id=group_id)
		members = Member.objects.filter(group__id=group_id)

		#get chat content
		group_chat = Chat.objects.filter(group__id=group_id)

		#notes
		notes = Note.objects.filter(owner__id=group_id).order_by('-id')
		
		return render(request, 'index.html', {'group_chat': group_chat, 'user': user, 'group': group, 'group_name': group_name, 'members': members, 'notes': notes, 'group_id': group_id})
	else:
		return redirect('signin')

def profile(request):
	if request.user.is_authenticated():
		user_id = request.user.id
		user = Users.objects.get(user__id=user_id)
		group = Member.objects.filter(member__pk=user.pk)
		print(group.query)
		return render(request, 'profile.html', { 'user': user, 'group': group})
	else:
		return redirect('signin')


def respond_to_websockets(message):
	pass