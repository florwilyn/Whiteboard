from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from whiteboard.models import Group
from whiteboard.models import Member
from .models import Users
from whiteboard.models import Note

def add_group(request):
	if request.method == "POST":
		groupname = request.POST.get('groupname', None)
		user_id = request.POST.get('user', None)

		user = Users.objects.get(id=user_id)
		newgroup = Group(owner=user, group_name=groupname)
		newgroup.save()
		addowner = Member(group=newgroup, member=user)
		addowner.save()

		return JsonResponse({'newgroup': newgroup.group_name, 'id': newgroup.id})

def login(request):
	return render(request, 'login.html')

def signup(request):
	return render(request, 'signup.html')
