# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0013_auto_20150827_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancer',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
        migrations.AlterField(
            model_name='semester',
            name='admin',
            field=models.OneToOneField(related_name='owned_org', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='semester',
            name='season',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall')], max_length=2),
        ),
    ]
