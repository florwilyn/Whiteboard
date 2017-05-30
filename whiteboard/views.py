from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat
from .models import Group
from .models import Member
from django.contrib.auth.models import User
from .models import Note
from user_profile.models import Users
from django.contrib.auth import authenticate, login, logout

def Post(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			msg = request.POST.get('msgbox', None)
			recipient = request.POST.get('recipient', None)

			group = Group.objects.get(pk=recipient)
			user_id = request.user
			user = Users.objects.get(user__id=user_id.id)
			c = Chat(sender=user, content=msg, group=group)
			if msg != '':
	 			c.save()

			return JsonResponse({ 'msg': msg, 'sender': c.sender.first_name + " " + c.sender.last_name, 'date_sent': c.date_sent, 'id': c.sender.user.id, 'photo': c.sender.prof_pic.url })
		else:
			return HttpResponse('Request must be POST.')
	return redirect('signin')

def add_member(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			username = request.POST.get('user', None)
			group_id = request.POST.get('group', None)


			togroup = Group.objects.get(pk=group_id)

			try:
				user = Users.objects.get(user__username=username)

				try: 
					is_member = Member.objects.get(group=togroup,member=user)
					return JsonResponse({'error': username + " is already a member"})
				except:
					newmember = Member(group=togroup, member=user)
					newmember.save()
			except:
				return JsonResponse({'error': "Username does not exist."})

			return JsonResponse({'photo': newmember.member.prof_pic.url, 'first_name': newmember.member.first_name})
	return redirect('signin')

def add_note(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			note = request.POST.get('note', None)
			group_id = request.POST.get('group', None)

			att  = request.FILES.get('attachment', None)

			togroup = Group.objects.get(pk=group_id)

			newnote = Note(owner=togroup, note=note, attachment=att)
			newnote.save()

			return JsonResponse({'note': newnote.note})
	return redirect('signin')

def chat(request,group_id):
	if request.user.is_authenticated():
		#get chat content
		group_chat = Chat.objects.filter(group__id=group_id)
		user_id = request.user.id
		user = Users.objects.get(user__id=user_id)
		return render(request, 'chat.html', {'group_chat': group_chat, 'user': user})
	return redirect('signin')

def notes(request,group_id):
	if request.user.is_authenticated():
		notes = Note.objects.filter(owner__id=group_id).order_by('-id')

		return render(request, 'notes.html', {'notes': notes})
	return redirect('signin')

def members(request,group_id):
	if request.user.is_authenticated():
		members = Member.objects.filter(group__id=group_id)

		return render(request, 'members.html', {'members': members})
	return redirect('signin')

def leave(request,group_id):
	if request.user.is_authenticated():
		user = request.user.id
		user_ = Users.objects.get(user__id=user)
		Member.objects.filter(group__id=group_id,member__id=user_.id).delete()

		return redirect("/")
	return redirect('signin')

def delete_note(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			notes = request.POST.getlist('notes[]') 
			print(".........................................................")
			print(notes)
			Note.objects.filter(id__in=notes).delete()
		
		return JsonResponse({'note': notes})
	return redirect('signin')
