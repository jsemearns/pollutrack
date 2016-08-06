# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('images', models.ManyToManyField(to='images.ImageUploads')),
            ],
        ),
        migrations.CreateModel(
            name='PollutionSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('radius', models.FloatField(null=True, blank=True)),
                ('severity', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('victim_count', models.PositiveIntegerField(null=True, blank=True)),
                ('center', models.OneToOneField(related_name='source', to='pollution.Coordinates')),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('images', models.ManyToManyField(to='images.ImageUploads')),
                ('pollution', models.ForeignKey(related_name='victims', to='pollution.PollutionSource')),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='pollution',
            field=models.ManyToManyField(to='pollution.PollutionSource'),
        ),
    ]
