# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0003_auto_20150811_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='csum',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
