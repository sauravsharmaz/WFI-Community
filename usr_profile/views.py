from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def usrProfile(request,usr_name):
    return HttpResponse(f'user profile is {usr_name}')