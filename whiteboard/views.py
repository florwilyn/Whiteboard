from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat
from .models import Group
from .models import Member
from django.contrib.auth.models import User
from .models import Note
from user_profile.models import Users

def Post(request):
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

def add_member(request):
	if request.method == "POST":
		username = request.POST.get('user', None)
		group_id = request.POST.get('group', None)

		print(group_id)
		togroup = Group.objects.get(pk=group_id)
		user = Users.objects.get(user__username=username)

		# print(group);
		newmember = Member(group=togroup, member=user)
		newmember.save()

		return JsonResponse({'photo': newmember.member.prof_pic.url, 'first_name': newmember.member.first_name})

def add_note(request):
	if request.method == "POST":
		note = request.POST.get('note', None)
		group_id = request.POST.get('group', None)

		togroup = Group.objects.get(pk=group_id)

		newnote = Note(owner=togroup, note=note)
		newnote.save()

		return JsonResponse({'note': newnote.note})

def chat(request,group_id):
	#get chat content
	group_chat = Chat.objects.filter(group__id=group_id)
	user_id = request.user.id
	user = Users.objects.get(user__id=user_id)
	return render(request, 'chat.html', {'group_chat': group_chat, 'user': user})