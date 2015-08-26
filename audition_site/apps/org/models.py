# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import managers
from . import afx_user
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
	org_name = models.CharField(max_length=50)
	semester = models.CharField(max_length=2, choices=SEMESTERS)
	admin_name = models.CharField(max_length=50)
	def email(self):
		return self.user.email

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
	numClaims = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
        )
	eligible = (castingGroup != None)
	def eligibleTraining():
		return eligible and numClaims.counts < 2
	def allSet():
		return (not eligible and numClaims == 0) or (numClaims == 1 or numClaims == 2)

class Team(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="teams",
		)
	dancers = models.ManyToManyField(
		Dancer,
		related_name="teams")
	name = models.CharField(max_length=50)
	isProjects = models.BooleanField(default=False)
	isTraining = not isProjects

class Director(models.Model):
	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_director_for_new_user(sender, created, instance, **kwargs):
	    if created:
	        director = Director(user=instance)
	        director.save()
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name="director",
		blank=True,
	)
	org = models.ForeignKey(
		Organization,
		related_name="directors",
		)
	team = models.ForeignKey(Team)
	#Attributes - Mandatory
	name = models.CharField(max_length=50)
	email = models.EmailField

