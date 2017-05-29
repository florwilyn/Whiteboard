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
	if request.user.is_authenticated:
		return redirect('/') # Or Base URL for Profile

    if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)

			### Use this if you want user to have a name or not
			# if user.get_full_name() == '':
				# return redirect(reverse('edit_profile'))
			return redirect('/')
		else:
			context['error'] = 'Invalid Username or Password'
			context['username'] = username
	return render(request, 'registration/sign_in.html', context=context)

	return render(request, 'login.html', context)

def signup(request):
	# Note: On the HTML, see if you can add like a redirect to login if they have an account
	if request.user.is_authenticated:
        return redirect('/') # Or Base URL for Profile
    context = {}
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = UserCreationForm()
    context['form'] = form

	return render(request, 'signup.html', context=context)
