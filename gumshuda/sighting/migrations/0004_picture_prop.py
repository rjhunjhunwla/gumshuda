# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sighting', '0003_auto_20150819_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='prop',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
