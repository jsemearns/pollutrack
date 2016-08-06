# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('latitude', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollutionSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('address', models.TextField(blank=True)),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('center', models.OneToOneField(related_name='source', to='pollution.Coordinates')),
                ('images', models.ManyToManyField(to='images.ImageUploads')),
                ('owner', models.ForeignKey(related_name='pollution_reports', to=settings.AUTH_USER_MODEL)),
                ('user_approved', models.ManyToManyField(related_name='approved_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
