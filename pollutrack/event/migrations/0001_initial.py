# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollution', '0002_pollutionsource_is_verified'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('slogan', models.CharField(max_length=150, blank=True)),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('donation_goal', models.FloatField(default=0)),
                ('donation_gathered', models.FloatField(default=0)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Open'), (1, b'Ongoing'), (2, b'Done')])),
                ('approval', models.IntegerField(default=0, choices=[(0, b'Pending'), (1, b'Live'), (2, b'Rejected')])),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('after_images', models.ManyToManyField(related_name='events_after', to='images.ImageUploads')),
                ('before_images', models.ManyToManyField(related_name='events_before', to='images.ImageUploads')),
                ('owner', models.ForeignKey(related_name='events', to=settings.AUTH_USER_MODEL)),
                ('pollution_source', models.ForeignKey(related_name='events', to='pollution.PollutionSource')),
                ('volunteers', models.ManyToManyField(related_name='joined_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Freebie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('event', models.ForeignKey(related_name='freebies', to='event.Event')),
                ('images', models.ManyToManyField(related_name='freebies', to='images.ImageUploads')),
            ],
        ),
    ]
