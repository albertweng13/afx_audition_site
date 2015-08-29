# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0016_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='season',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], max_length=6),
        ),
    ]
