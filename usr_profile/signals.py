from App_wfi_Community import signals
from django.dispatch import Signal,receiver
from django.db import models
from usr_profile.models import proFile

create_profile= Signal(providing_args=['usr'])

@receiver(create_profile)
def make_profile(usr,**kwargs):
    username= usr.username
    mk_prof_ob= proFile(usr=usr,usrname= username)
    mk_prof_ob.save()