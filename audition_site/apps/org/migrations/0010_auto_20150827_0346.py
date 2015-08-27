# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0009_auto_20150827_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castinggroup',
            name='semester',
            field=models.ForeignKey(related_name='castingGroups', to='org.Semester', null=True),
        ),
        migrations.AlterField(
            model_name='dancer',
            name='semester',
            field=models.ForeignKey(related_name='dancers', to='org.Semester', verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='team',
            name='semester',
            field=models.ForeignKey(blank=0, related_name='teams', to='org.Semester'),
        ),
    ]
