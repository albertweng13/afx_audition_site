# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0004_auto_20150826_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancer',
            name='email',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
