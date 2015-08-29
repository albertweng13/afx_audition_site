# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0014_auto_20150828_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='season',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], max_length=6),
        ),
    ]
