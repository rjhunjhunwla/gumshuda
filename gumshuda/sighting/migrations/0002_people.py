# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0001_initial'),
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
            ],
        ),
    ]
