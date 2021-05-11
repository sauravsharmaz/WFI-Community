from App_wfi_Community.models import Upvote
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Upvote

@receiver(pre_save, sender= Upvote)
def upvt_save_handler(sender, instance, **kwargs):
    pass
