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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('numClaims', models.PositiveIntegerField(verbose_name='interaction', default=0)),
                ('castingGroup', models.ForeignKey(blank=True, to='org.CastingGroup', related_name='dancers')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('semester', models.CharField(choices=[('Sp', 'Spring'), ('Su', 'Summer'), ('Fa', 'Fall')], max_length=2)),
                ('admin', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='owned_org')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('isProjects', models.BooleanField(default=False)),
                ('dancers', models.ManyToManyField(related_name='teams', to='org.Dancer')),
                ('org', models.ForeignKey(related_name='teams', to='org.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='org',
            field=models.ForeignKey(related_name='directors', to='org.Organization'),
        ),
        migrations.AddField(
            model_name='director',
            name='organization',
            field=models.ForeignKey(to='org.Organization'),
        ),
        migrations.AddField(
            model_name='director',
            name='team',
            field=models.ForeignKey(to='org.Team'),
        ),
        migrations.AddField(
            model_name='director',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, related_name='director'),
        ),
        migrations.AddField(
            model_name='dancer',
            name='org',
            field=models.ForeignKey(related_name='dancers', to='org.Organization'),
        ),
        migrations.AddField(
            model_name='castinggroup',
            name='org',
            field=models.ForeignKey(related_name='castingGroups', to='org.Organization'),
        ),
    ]
