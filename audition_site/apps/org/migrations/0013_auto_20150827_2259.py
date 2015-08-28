# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0012_auto_20150827_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1),
        ),
    ]
