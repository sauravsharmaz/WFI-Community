from django.shortcuts import render
from django.http import request,HttpResponseRedirect
# for user creation & login form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# for user related Queries
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
from usr_profile import signals

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
            signals.create_profile.send(sender=None,usr=request.user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Either the user name is not available or you may have filled the form incorrectly')
    else:
        form = UserCreationForm()
        context= {'form':form}
        return render(request,'authentication/register_Page.html',context)

# # login page
# def login_page(request):
#   if request.user.is_authenticated:
#       return redirect('Home_page')
#   if request.method == 'POST':
#       username= request.POST['username']
#       password= request.POST['password']
#       # returns user if credentials are valid
#       user= authenticate(request, username=username, password= password)
#       # check if user var contains the user
#       if user is not None:
#           login(request, user)
#           return redirect(reverse('Home_page'))
#       else:
#           return HttpResponse('Invalid credentials')
    
#   return render(request,'authentication/login.html')


# login page
def login_page(request):
    # check if user is logged in already
    if request.user.is_authenticated:
        return redirect('Home_page')

    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        # returns user if credentials are valid
        user= authenticate(request, username=username, password= password)
        # check if user var contains the user
        if user is not None:
            login(request, user)
            return redirect(reverse('Home_page'))
        else:
            return HttpResponse('Invalid credentials')
    # check if the user is redirected
    
    try:
        # Get the data from session storage
        redirected= request.session.get('redirected')
        if redirected == 'True':
            del request.session['redirected'] # delete the session key to avoid errors
            data= {'warning':"please login first"}
            return render(request,'authentication/login.html',data)
    except Exception as e:
        pass    
    return render(request,'authentication/login.html')
    
        

# logout Page
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))