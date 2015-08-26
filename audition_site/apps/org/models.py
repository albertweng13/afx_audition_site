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
    year = models.PositiveIntegerField()
    # choosingProjects = models.BooleanField(default=True)

    @property
    def choosingProjects(self):
        for x in self.teams.all():
            if x.level == 'P' and not x.allSet:
                return True
        return False

    @property
    def allSet(self):
        for x in self.teams.all():
            if not x.allSet:
                return False
        for x in self.dancers.all():
            if not x.allSet:
                return False
        return True
    
    @property
    def admin_name(self):
        return self.admin.username

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")
        # ordering = ("user",)
 
    def __str__(self):
        return self.org_name

class CastingGroup(models.Model):
    org = models.ForeignKey(
        Organization,
        related_name="castingGroups"
    )
    video_link = models.URLField(blank=True)

    class Meta:
        verbose_name = _("Casting Group")
        verbose_name_plural = _("Casting Groups")
        # ordering = ("user",)
 
    def __str__(self):
        return str(self.id)

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
        blank=True,
        null=True
    )
    email = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=50)

    @property
    def auditioned(self):
        return self.casting_group != None

    @property
    def eligibleTraining(self):
        return self.auditioned and len([x for x in self.teams.all() if x.level=='P']) < 2

    @property
    def eligible(self):
        return (self.auditioned or (not self.org.choosingProjects and self.eligibleTraining))

    @property
    def numClaims(self):
        return self.teams.count()

    @property
    def allSet(self):
        return (not self.eligible and self.numClaims == 0) or ((self.numClaims == 1) or (self.numClaims == 2))

    class Meta:
        verbose_name = _("Dancer")
        verbose_name_plural = _("Dancers")
        # ordering = ("user",)
 
    def __str__(self):
        return self.name

class Team(models.Model):

    org = models.ForeignKey(
        Organization,
        blank=0,
        related_name="teams"
        )

    LEVELS = (
        ('T', 'Training'),
        ('P', 'Projects')
    )
    level = models.CharField(max_length=1, choices=LEVELS)
    name = models.CharField(max_length=50)
    allSet = models.BooleanField(default=False)

    # # limit_choices = {'eligible': True}
    # # if level == 'T':
    # #     limit_choices['eligibleTraining': True]
    # def limit_choices():
    #     choices = {'eligible': True}
    #     if level == 'T':
    #         choices['eligibleTraining': True]
    #     return choices

    dancers = models.ManyToManyField(
        Dancer,
        blank = True,
        related_name="teams"#,
        #limit_choices_to = limit_choices
        )

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        # ordering = ("user",)
 
    def __str__(self):
        return self.name

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
    team = models.ForeignKey(
        Team,
        related_name="directors") #TODO
    #Attributes - Mandatory
    name = models.CharField(max_length=50)
    #email = models.EmailField

    class Meta:
        verbose_name = _("Director")
        verbose_name_plural = _("Directors")
        # ordering = ("user",)
 
    def __str__(self):
        return self.name

