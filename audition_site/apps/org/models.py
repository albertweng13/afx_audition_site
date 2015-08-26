# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
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
	admin = models.ForeignKey(
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
	
	@property
	def admin_name(self):
		return self.admin.username

class CastingGroup(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="castingGroups"
	)
	video_link = models.URLField(blank=True)

	# # in logic
	# org = get_current_org()
	# cg1 = CastingGroup(org=my_org)
	# cg1.save()
	# org.castingGroups.all()

class Dancer(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="dancers"
		)
	casting_group = models.ForeignKey(
		CastingGroup,
		related_name = "dancers",
		blank=True
	)
	name = models.CharField(max_length=50)
	email = models.EmailField

	@property
	def eligible(self):
		return (self.castingGroup != None)

	def eligibleTraining(self):
		return eligible and len([x for x in self.teams.all() if x.level=='P']) < 2

	def allSet(self):
		return (not eligible and numClaims == 0) or (numClaims == 1 or numClaims == 2)

class Team(models.Model):
	org = models.ForeignKey(
		Organization,
		blank=0,
		related_name="teams",
		)
	dancers = models.ManyToManyField(
		Dancer,
		blank = True,
		related_name="teams")
	TRAINING = 'T'

	LEVELS = (
		('T', 'Training'),
		('P', 'Projects')
	)
	level = models.CharField(max_length=1, choices=LEVELS)
	name = models.CharField(max_length=50)

# Team(level=Team.TRAINING)

class Director(models.Model):
	# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
	# def create_director_for_new_user(sender, created, instance, **kwargs):
	#     if created:
	#         director = Director(user=instance)
	#         director.save()
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name="director",
		blank=True,
	)
	org = models.ForeignKey(
		Organization,
		related_name="directors",
		)
	team = models.ForeignKey(Team) #TODO
	#Attributes - Mandatory
	name = models.CharField(max_length=50)
	email = models.EmailField

