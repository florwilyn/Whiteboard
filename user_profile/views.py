from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from whiteboard.models import Group
from whiteboard.models import Member
from .models import Users
from whiteboard.models import Note
from django.contrib.auth import authenticate, login, logout

def add_group(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			groupname = request.POST.get('groupname', None)
			user_id = request.POST.get('user', None)

			user = Users.objects.get(id=user_id)
			newgroup = Group(owner=user, group_name=groupname)
			newgroup.save()
			addowner = Member(group=newgroup, member=user)
			addowner.save()

			return JsonResponse({'newgroup': newgroup.group_name, 'id': newgroup.id})
	return redirect('signin')

def signin(request):
	error = ""
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return redirect('/')
		error = "Invalid username/password."
	return render(request, 'login.html', {'error': error})

def signout(request):
	logout(request)
	return redirect('signin')

def signup(request):
	return render(request, 'signup.html')
