from django.shortcuts import render, redirect, HttpResponse
from . import models
from models import User, Friend
import datetime

# Create your views here.
def index(request):
	request.session.pop('id', None)
	# request.session.pop('errors', None)
	# request.session.pop('login_errors', None)
	request.session.pop('alias', None)
	return render(request, 'friends/index.html')

def register(request):
	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = request.POST['password']
	confirmPW = request.POST['confirmPW']
	dob = request.POST['dob']
	result = User.userMgr.validateRegis(name=name, alias=alias, email=email, password=password, confirmPW=confirmPW, dob=dob)
	if result[0]:
		request.session['alias'] = alias
		request.session.pop('errors', None)
		request.session['id'] = result[1].id
		return redirect('/friends')
	else:
		request.session['errors'] = result[1]
		return redirect('/')

def login(request):
	login_email = request.POST['login_email']
	login_pw = request.POST['login_pw']
	result = User.userMgr.validateLogin(login_email=login_email, login_pw=login_pw)
	pw_hash = User.userMgr.filter(email=login_email).values('pw_hash')
	if result[0]:
		getUser = result[1]
		request.session['id'] = getUser.id
		request.session['alias'] = getUser.alias
		request.session.pop('login_errors', None)
		return redirect('/friends')
	else:
		request.session['login_errors'] = result[1]
		return redirect('/')

def showDashboard(request):
	currentUser = request.session['id']
	friends = User.userMgr.filter(pk=currentUser).values('myself__user2__alias', 'myself__user2__id')
	nonFriends = User.userMgr.exclude(pk=currentUser).exclude(myfriend__user=currentUser)
	# anyfriends = models.Friend.objects.filter(user=currentUser)
	# request.session['anyfriends'] = anyfriends.user2
	context = {'friends':friends, 'nonFriends':nonFriends}
	return render(request, 'friends/dashboard.html', context)

def addFriend(request, id):
	currentUser = User.userMgr.get(pk=request.session['id'])
	newfriend = User.userMgr.get(pk=id)
	addfriend = models.Friend.objects.create(user=currentUser, user2=newfriend)
	addOther = models.Friend.objects.create(user=newfriend, user2=currentUser)
	return redirect('/friends')

def showProfile(request, id):
	getUser = User.userMgr.get(pk=id)
	context = {'getUser':getUser}
	return render(request, 'friends/showprofile.html', context)

def destroy(request, id):
	currentUser = User.userMgr.get(pk=request.session['id'])
	deleteFriend = models.Friend.objects.filter(user=currentUser, user2=id).delete()
	deleteOther = models.Friend.objects.filter(user=id, user2=currentUser).delete()
	return redirect('/friends')

def logout(request):
	request.session.pop('errors', None)
	request.session.pop('alias', None)
	request.session.pop('login_errors', None)
	request.session.pop('id', None)
	return redirect('/')