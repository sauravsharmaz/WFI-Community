from App_wfi_Community.models import DownVote_record, DownVote, Upvote, Upvote_record


def chk_usr_dnvt_rec(ans, usr):
    try:
        ob = DownVote_record.objects.get(ans=ans, usr=usr)
        ob.delete()
        return "yes"
    except Exception as e:
        return "no"

def chk_usr_upvt_rec(ans,usr):
    try:
        ob= Upvote_record.objects.get(ans=ans,usr=usr)
        ob.delete()
        return "yes"
    except Exception as e:
        return "no"

def delete_downVote(ans):
    dnvt = DownVote.objects.get(answer=ans)
    iD = dnvt.id
    val = dnvt.value - 1
    ob = DownVote(id=iD, value=val, answer=ans)
    ob.save()

def delete_upvote(ans):
    upvt= Upvote.objects.get(answer= ans)
    iD= upvt.id
    val= upvt.value - 1
    ob = Upvote(id=iD,value=val,answer=ans)
    ob.save()