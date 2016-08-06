from django.db.models.signals import post_save
from django.contrib.auth.models import User

from profile.models import Profile


def create_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)