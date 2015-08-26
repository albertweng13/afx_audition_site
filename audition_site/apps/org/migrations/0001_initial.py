# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CastingGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('video_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('casting_group', models.ForeignKey(related_name='dancers', to='org.CastingGroup', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('org_name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('Sp', 'Spring'), ('Su', 'Summer'), ('Fa', 'Fall')], max_length=2)),
                ('year', models.PositiveIntegerField()),
                ('admin', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owned_org')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('level', models.CharField(choices=[('T', 'Training'), ('P', 'Projects')], max_length=1)),
                ('name', models.CharField(max_length=50)),
                ('dancers', models.ManyToManyField(related_name='teams', to='org.Dancer', blank=True)),
                ('org', models.ForeignKey(related_name='teams', to='org.Organization', blank=0)),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='org',
            field=models.ForeignKey(to='org.Organization', related_name='directors'),
        ),
        migrations.AddField(
            model_name='director',
            name='team',
            field=models.ForeignKey(to='org.Team'),
        ),
        migrations.AddField(
            model_name='director',
            name='user',
            field=models.OneToOneField(related_name='director', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='dancer',
            name='org',
            field=models.ForeignKey(to='org.Organization', related_name='dancers'),
        ),
        migrations.AddField(
            model_name='castinggroup',
            name='org',
            field=models.ForeignKey(to='org.Organization', related_name='castingGroups'),
        ),
    ]
