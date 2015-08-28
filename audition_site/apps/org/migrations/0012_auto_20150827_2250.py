# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0011_castinggroup_dancer_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='dancer',
            name='gender',
            field=models.CharField(max_length=1, default='', choices=[('F', 'Female'), ('M', 'Male'), ('-', '--')]),
        ),
        migrations.AddField(
            model_name='dancer',
            name='phone',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
