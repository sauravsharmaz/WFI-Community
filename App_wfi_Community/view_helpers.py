from App_wfi_Community.models import Upvote_record, Upvote


def check_upvote_record(usr, ans_ob):
    try:
        upvt_rec = Upvote_record.objects.get(ans=ans_ob, usr=usr)
        print('upvote record for this user on this ans found')
        # return upvt_rec
        return "yes"
    except Upvote_record.DoesNotExist:
        print('the record with the provided usr not exist')
        return "no"
    except Upvote_record.MultipleObjectsReturned:
        print('there are more than one record for this usr and ans')
        return "yes"
    except Exception as e:
        print('there is no upvote record for this user')
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
        print('updated upvote value')
    except Exception as e:
        val= 1
        ob = Upvote(value=val,answer=ansob)
        ob.save()
        print('no upvote value so created a one and saved that')

