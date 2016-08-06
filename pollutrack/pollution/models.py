from django.db import models
from images.models import ImageUploads


# Create your models here.
class Coordinates(models.Model):
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'pollution'

class PollutionSource(models.Model):
    radius = models.FloatField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    center = models.OneToOneField(Coordinates, related_name='source')
    victim_count = models.PositiveIntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        app_label = 'pollution'


class Victim(models.Model):
    pollution = models.ForeignKey(PollutionSource, related_name='victims')
    images = models.ManyToManyField(ImageUploads)

    class Meta:
        app_label = 'pollution'


class Disease(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pollution = models.ManyToManyField(PollutionSource)
    images = models.ManyToManyField(ImageUploads)

    class Meta:
        app_label = 'pollution'
