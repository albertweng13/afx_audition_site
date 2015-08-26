# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='org',
        ),
        migrations.AlterField(
            model_name='director',
            name='team',
            field=models.ForeignKey(related_name='directors', to='org.Team'),
        ),
    ]
