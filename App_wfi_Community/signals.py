from django.dispatch import Signal, receiver
from .signal_helpers import chk_usr_dnvt_rec, chk_usr_upvt_rec, delete_downVote, delete_upvote

from .models import Upvote

delete_downvote = Signal(providing_args=['ans', 'usr'])
delete_upVote = Signal(providing_args=['ans','usr'])

@receiver(delete_downvote)
def upvt_save_handler(ans, usr, **kwargs):
    if chk_usr_dnvt_rec(ans, usr) == "yes":
        delete_downVote(ans)

@receiver(delete_upVote)
def dnvt_save_handler(ans,usr,**kwargs):
    if chk_usr_upvt_rec(ans,usr) == "yes":
        delete_upvote(ans)