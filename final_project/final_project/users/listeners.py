'''
@receiver(user_logged_in)
def login_user(user, request, **kwargs):
    user.SiteUser.login_count = user.SiteUser.login_count + 1
    user.SiteUser.save()
user_logged_in.connect(login_user, user = SiteUser)

'''

from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import SiteUser


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        SiteUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if not created:
        instance.siteuser.save()



def login_user(sender, instance, **kwargs):
    instance.siteuser.login_count = instance.siteuser.login_count + 1
    instance.siteuser.save()


post_save.connect(login_user, sender=User)
