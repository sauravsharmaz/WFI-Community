from django.shortcuts import render
from django.http import request,HttpResponseRedirect
# for user creation & login form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# for user related Queries
from django.contrib.auth.models import User
from django.urls import reverse


# imports for test purpose
from django.http import HttpResponse

# Create your views here.

# register page 
def register_Page(request):
	if request.method == 'POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username= request.POST['username']
			password= request.POST['password1']
			user= authenticate(request,username=username,password=password)
			login(request,user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Either the user name is not available or you may have filled the form incorrectly')
	else:
		form = UserCreationForm()
		context= {'form':form}
		return render(request,'authentication/register_Page.html',context)

# login page
def login_page(request):
	if request.method == 'POST':
		username= request.POST['username']
		password= request.POST['password']
		# returns user if credentials are valid
		user= authenticate(request, username=username, password= password)
		# check if user var contains the user
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('Invalid credentials')

	return render(request,'authentication/login.html')

# logout Page
def log_out(request):
	logout(request)
	return HttpResponseRedirect(reverse('login_page'))