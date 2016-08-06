# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('pollution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutionsource',
            name='after_images',
            field=models.ManyToManyField(related_name='after_pollutions', to='images.ImageUploads'),
        ),
        migrations.AddField(
            model_name='pollutionsource',
            name='is_fixed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pollutionsource',
            name='images',
            field=models.ManyToManyField(related_name='pollutions', to='images.ImageUploads'),
        ),
    ]
