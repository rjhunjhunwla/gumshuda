# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('father_name', models.CharField(max_length=256)),
                ('mother_name', models.CharField(max_length=256)),
                ('age', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField()),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('data', models.BinaryField()),
                ('csum', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='reported_sighting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.TextField()),
                ('people_id', models.ForeignKey(to='sighting.people')),
                ('picture_id', models.ForeignKey(to='sighting.picture')),
            ],
        ),
        migrations.CreateModel(
            name='sighting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loc', models.CharField(max_length=64)),
                ('picture_id', models.ForeignKey(to='sighting.picture')),
            ],
        ),
        migrations.CreateModel(
            name='source_picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('people_id', models.ForeignKey(to='sighting.people')),
                ('picture_id', models.ForeignKey(to='sighting.picture')),
            ],
        ),
    ]
