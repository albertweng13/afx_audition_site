# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0007_auto_20150826_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='choosingProjects',
        ),
    ]
