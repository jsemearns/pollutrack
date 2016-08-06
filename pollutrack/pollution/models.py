from django.db import models
from django.contrib.auth.models import User

from images.models import ImageUploads


# Create your models here.
class Coordinates(models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'pollution'


class PollutionSource(models.Model):
    owner = models.ForeignKey(User, related_name='pollution_reports')
    description = models.TextField(blank=True)
    center = models.OneToOneField(Coordinates, related_name='source')
    is_verified = models.BooleanField(default=False)
    is_fixed = models.BooleanField(default=False)
    images = models.ManyToManyField(ImageUploads, related_name='pollutions')
    after_images = models.ManyToManyField(
        ImageUploads, related_name='after_pollutions')
    address = models.TextField(blank=True)
    when = models.DateTimeField(auto_now_add=True)
    user_approved = models.ManyToManyField(User, related_name='approved_posts')

    class Meta:
        app_label = 'pollution'
