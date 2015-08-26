# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0006_auto_20150826_0303'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='choosingProjects',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='team',
            name='allSet',
            field=models.BooleanField(default=False),
        ),
    ]
