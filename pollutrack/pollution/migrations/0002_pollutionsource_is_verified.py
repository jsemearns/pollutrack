# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutionsource',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
