# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='valid',
        ),
    ]
