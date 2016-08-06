from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from images.models import ImageUploads
from pollution.models import PollutionSource


EVENT_STATUS = ((0, 'Open'), (1, 'Ongoing'), (2, 'Done'))
EVENT_APPROVAL = ((0, 'Pending'), (1, 'Live'), (2, 'Rejected'))

class Event(models.Model):
    owner = models.ForeignKey(User, related_name='events')
    pollution_source = models.ForeignKey(
        PollutionSource, related_name='events')
    description = models.TextField(blank=True)
    slogan = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    donation_goal = models.FloatField(default=0)
    donation_gathered = models.FloatField(default=0)
    status = models.IntegerField(choices=EVENT_STATUS, default=0)
    approval = models.IntegerField(choices=EVENT_APPROVAL, default=0)
    volunteers = models.ManyToManyField(User, related_name='joined_events')
    before_images = models.ManyToManyField(
        ImageUploads, related_name='events_before')
    after_images = models.ManyToManyField(
        ImageUploads, related_name='events_after')
    when = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'event'


class Freebie(models.Model):
    event = models.ForeignKey(Event, related_name='freebies')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    images = models.ManyToManyField(ImageUploads, related_name='freebies')
