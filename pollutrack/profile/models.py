from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


USER_TYPES = ((0, 'Volunteer'), (1, 'Company'), (2, 'Organization'))

class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    user_type = models.IntegerField(choices=USER_TYPES, default=0)
    profile_image = models.ImageField(
        blank=True, upload_to=settings.PROFILE_IMAGE_UPLOAD_PATH)
    cover_image = models.ImageField(
        blank=True, upload_to=settings.PROFILE_COVER_UPLOAD_PATH)

    class Meta:
        app_label = 'profile'
