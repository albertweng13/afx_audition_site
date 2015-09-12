# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0010_auto_20150827_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='castinggroup',
            name='dancer_ids',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
