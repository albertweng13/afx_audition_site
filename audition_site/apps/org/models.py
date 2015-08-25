# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
 
from . import managers
# Create your models here.

#class MyModel(models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String

class Organization(models.Model):
	admin = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name = "owned_org"
		)

	SEMESTERS = (
		('Sp', 'Spring'),
		('Su', 'Summer'),
		('Fa', 'Fall')
	)
	name = models.CharField(max_length=50)
	semester = models.CharField(max_length=2, choices=SEMESTERS)

class CastingGroup(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="castingGroups"
		)
	groupId = models.PositiveIntegerField
	videoLink = models.URLField

class Dancer(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="dancers"
		)
	castingGroup = models.ForeignKey(
		CastingGroup,
		related_name = "dancers",
		blank=True
		)
	name = models.CharField(max_length=50)
	email = models.EmailField
	dancerId = models.PositiveIntegerField
	eligible = (castingGroup != None)
	eligibleTraining = (eligible and projects.counts < 2)
	numClaims = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
        )
	allSet = (not eligible and numClaims == 0) or (numClaims == 1 or numClaims == 2)

class Team(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="teams",
		)
	dancers = models.ManyToManyField(
		Dancer,
		related_name="teams")
	name = models.CharField(max_length=50)

class Exec(models.Model):
	#Relations
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		blank=True,
		related_name="exec",
	)
	org = models.ForeignKey(
		Organization,
		related_name="exec",
		)
	name = models.CharField(max_length=50)
	email = models.EmailField

class Director(models.Model):
	#Relations
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name="director",
		blank=True,
	)
	org = models.ForeignKey(
		Organization,
		related_name="directors",
		)
	organization = models.ForeignKey(Organization)
	team = models.ForeignKey(Team)
	#Attributes - Mandatory
	name = models.CharField(max_length=50)
	email = models.EmailField
	isExec = models.BooleanField(default = False)

