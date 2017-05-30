from django.contrib.auth.models import User
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

def edit_profile(request):
	if request.user.is_authenticated():
		user_id = request.user.id
		user = Users.objects.get(user__id=user_id)
		group = Member.objects.filter(member__pk=user.pk)
		return render(request, 'edit_profile.html', {'user': user, 'group': group})
	else:
		return redirect('signin')

def edit(request):
	if request.user.is_authenticated():
		if request.method == 'POST':
			user = Users.objects.get(user__id=request.user.id)
			user_ = user.user

			fname = request.POST.get('fname', None)
			lname = request.POST.get('lname', None)
			username = request.POST.get('username', None)
			pic = request.FILES.get('myfile', None)

			password = request.POST.get('password', None)

			if fname != '':
				user.first_name = fname
				
			if lname != '':
				user.last_name = lname

			if username != '':
				user_.username = username
				
			if password != '':
				user_.set_password(password)
			if pic != '':
				user.prof_pic = pic

			user.save()
			user_.save()

			return redirect('/')

def register(request):
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == "POST":
		username = request.POST.get('username',None)
		password = request.POST.get('password', None)

		try:
			user = User(username=username, password=password)
			user.save()
		except:
			return redirect('signin')

		fname = request.POST.get('fname', None)
		lname = request.POST.get('lname', None)

		new_user = Users(user=user,first_name=fname, last_name=lname)
		new_user.save()

		# u = authenticate(username=username, password=password)
		login(request, user)

		return redirect('edit')

