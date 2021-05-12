from django.core import exceptions
from App_wfi_Community.models import DownVote, DownVote_record, Upvote_record, Upvote


def chk_downvote_record(usr, ans):
    try:
        dnvt_rec= DownVote_record.objects.get(ans=ans,usr=usr)
        return "yes"
    except DownVote_record.MultipleObjectsReturned:
        return "yes"
    except Exception as e:
        return "no"

def save_to_downvote_record(usr, ans):
    val= 1
    ob= DownVote_record(val=val,ans=ans,usr=usr)
    ob.save()




def check_upvote_record(usr, ans_ob):
    try:
        upvt_rec = Upvote_record.objects.get(ans=ans_ob, usr=usr)
        return "yes"
    except Upvote_record.DoesNotExist:
        return "no"
    except Upvote_record.MultipleObjectsReturned:
        return "yes"
    except Exception as e:
        return "no"


def save_to_upvt_rec(usr, ansob):
    val= 1
    ob= Upvote_record(val=val,ans=ansob,usr=usr)
    ob.save()

def update_upvote(ansob):
    try:
        upvote= Upvote.objects.get(answer=ansob)
        val= upvote.value + 1
        ob= Upvote(id=upvote.id,answer=ansob,value=val)
        ob.save()
    except Exception as e:
        val= 1
        ob = Upvote(value=val,answer=ansob)
        ob.save()

def update_downvote(ansob):
    try:
        dnvt= DownVote.objects.get(answer=ansob)
        val= dnvt.value + 1
        ob= DownVote(id=dnvt.id,value=val,answer=ansob)
        ob.save()
    except Exception as e:
        val= 1
        ob= DownVote(value=val,answer=ansob)
        ob.save()