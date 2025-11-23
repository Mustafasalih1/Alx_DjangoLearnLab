from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import user
from . models import userprofile

@receiver(post_save,sender=user)
def creat_user_profile(sender,instance,created,""kwargs):
    if created:
        userprofile.objects.creat(user=inestance, role=Member)

@receiver(post_save,sender=user)
def save_user_profile(sender,instance,""kwargs):
    if hasattr(instance,'userprofile'):
        instance.user.profile.save()

