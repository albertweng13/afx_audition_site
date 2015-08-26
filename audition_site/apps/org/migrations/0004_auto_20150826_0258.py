# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0003_auto_20150826_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='casting_group',
            field=models.ForeignKey(related_name='dancers', null=True, to='org.CastingGroup', blank=True),
        ),
    ]
