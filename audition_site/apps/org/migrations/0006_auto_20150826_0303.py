# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0005_dancer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='castinggroup',
            options={'verbose_name_plural': 'Casting Groups', 'verbose_name': 'Casting Group'},
        ),
        migrations.AlterModelOptions(
            name='dancer',
            options={'verbose_name_plural': 'Dancers', 'verbose_name': 'Dancer'},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'verbose_name_plural': 'Directors', 'verbose_name': 'Director'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': 'Teams', 'verbose_name': 'Team'},
        ),
    ]
