from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

from images.models import ImageUploads


USER_TYPES = ((0, 'Volunteer'), (1, 'Company'), (2, 'Organization'))

class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    user_type = models.IntegerField(choices=USER_TYPES, default=0)
    profile_image = models.ForeignKey(ImageUploads, related_name='profile',
        blank=True, null=True)
    cover_image = models.ForeignKey(ImageUploads, related_name='profile_cover',
        blank=True, null=True)

    @property
    def profile_image_url(self):
        if self.profile_image:
            return self.profile_image.url
        return ''

    @property
    def profile_image_url(self):
        if self.cover_image:
            return self.cover_image.url
        return ''

    class Meta:
        app_label = 'profile'
