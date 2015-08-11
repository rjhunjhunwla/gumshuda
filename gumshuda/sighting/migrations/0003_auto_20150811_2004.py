# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0002_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
