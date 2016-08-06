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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.IntegerField(default=0, choices=[(0, b'Volunteer'), (1, b'Company'), (2, b'Organization')])),
                ('cover_image', models.ForeignKey(related_name='profile_cover', blank=True, to='images.ImageUploads', null=True)),
                ('owner', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ForeignKey(related_name='profile', blank=True, to='images.ImageUploads', null=True)),
            ],
        ),
    ]
