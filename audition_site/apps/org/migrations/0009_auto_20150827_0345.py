# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0008_remove_organization_choosingprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('season', models.CharField(max_length=2, choices=[('Sp', 'Spring'), ('Su', 'Summer'), ('Fa', 'Fall')])),
                ('year', models.PositiveIntegerField()),
                ('admin', models.ForeignKey(related_name='owned_org', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Semester',
                'verbose_name_plural': 'Semesters',
            },
        ),
        migrations.RemoveField(
            model_name='organization',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='castinggroup',
            name='org',
        ),
        migrations.RemoveField(
            model_name='dancer',
            name='org',
        ),
        migrations.RemoveField(
            model_name='team',
            name='org',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.AddField(
            model_name='castinggroup',
            name='semester',
            field=models.ForeignKey(related_name='castingGroups', null=True, blank=True, to='org.Semester'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='semester',
            field=models.ForeignKey(verbose_name='Semester', related_name='dancers', null=True, blank=True, to='org.Semester'),
        ),
        migrations.AddField(
            model_name='team',
            name='semester',
            field=models.ForeignKey(related_name='teams', null=True, blank=0, to='org.Semester'),
        ),
    ]
