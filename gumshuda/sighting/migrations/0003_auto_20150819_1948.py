# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0002_remove_people_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
