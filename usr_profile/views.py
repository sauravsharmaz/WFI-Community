from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from usr_profile.models import proFile

# Create your views here.
def usrProfile(request,usr_name):
    try:
        profile_ob= proFile.objects.get(usrname=usr_name)
        data= {
            "profile_ob": profile_ob
        }
        return render(request,'usr_profile/profile.html',data)
    except proFile.DoesNotExist:
        return HttpResponse('the user is admin & has not created profile yet')   
    except Exception as e:
        print('some exception while getting user',e)
        return HttpResponse('there is some error.. check terminal')