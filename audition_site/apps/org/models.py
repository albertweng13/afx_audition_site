# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import managers
from random import shuffle
# Create your models here.

#class MyModel(models.Model):
    # Relations
    # Attributes - Mandatory
    # Attributes - Optional
    # Object Manager
    # Custom Properties
    # Methods
    # Meta and String

class Semester(models.Model):
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name = "owned_org"
        )

    SEASONS = (
        ('Sp', 'Spring'),
        ('Su', 'Summer'),
        ('Fa', 'Fall')
    )
    season = models.CharField(max_length=2, choices=SEASONS)
    year = models.PositiveIntegerField()

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

    @property
    def conflictedDancers(self):
        return [x for x in self.dancers.all() if x.disputed==True]

    def randomizeDancersIntoTeams(self):
        #if(self.allSet):
            unclaimedDancers = self.dancers.filter(teams__isnull=True)#[x for x in self.dancers.all() if x.numClaims==0]
            teams = self.teams.filter(level='T')
            shuffle(teams)
            tCounter = 0
            for x in unclaimedDancers:
                print(str(x))
                if(tCounter>len(teams)-1):
                    tCounter = 0
                print(self.teams.count())
                #set unclaimedDancer to team[tCounter]
                team = teams[tCounter]
                print("Team: " + str(team))
                print("Dancer: " + str(x))
                team.dancers.add(x)
                team.save()
                tCounter += 1

    class Meta:
        verbose_name = _("Semester")
        verbose_name_plural = _("Semesters")
        # ordering = ("user",)
 
    def __str__(self):
        return ("AFX " + self.season + " " + str(self.year))

class CastingGroup(models.Model):
    semester = models.ForeignKey(
        Semester,
        related_name="castingGroups",
        null=True
    )
    video_link = models.URLField(blank=True)
    dancer_ids = models.CharField(max_length=50, default="")

    class Meta:
        verbose_name = _("Casting Group")
        verbose_name_plural = _("Casting Groups")
        # ordering = ("user",)
 
    def __str__(self):
        return str(self.id)

    @property
    def group_dancers(self):
        return self.dancers.all()

    # # in logic
    # org = get_current_org()
    # cg1 = CastingGroup(org=my_org)
    # cg1.save()
    # org.castingGroups.all()

class Dancer(models.Model):
    semester = models.ForeignKey(
        Semester,
        related_name="dancers",
        verbose_name="Semester"
        )
    casting_group = models.ForeignKey(
        CastingGroup,
        related_name = "dancers",
        blank=True,
        null=True
    )
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    phone = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDERS)

    @property
    def auditioned(self):
        return self.casting_group != None

    @property
    def eligibleTraining(self):
        return self.auditioned and len([x for x in self.teams.all() if x.level=='P']) < 2

    @property
    def eligible(self):
        return (self.auditioned or (not self.semester.choosingProjects and self.eligibleTraining))

    @property
    def numClaims(self):
        return self.teams.count()

    @property
    def allSet(self):
        return (not self.eligible and self.numClaims == 0) or ((self.numClaims == 1) or (self.numClaims == 2))

    @property
    def disputed(self):
        return self.numClaims>2

    class Meta:
        verbose_name = _("Dancer")
        verbose_name_plural = _("Dancers")
 
    def __str__(self):
        return self.name

class Team(models.Model):

    semester = models.ForeignKey(
        Semester,
        blank=0,
        related_name="teams",
        )

    LEVELS = (
        ('T', 'Training'),
        ('P', 'Projects')
    )
    level = models.CharField(max_length=1, choices=LEVELS)
    name = models.CharField(max_length=50)
    allSet = models.BooleanField(default=False)

    dancers = models.ManyToManyField(
        Dancer,
        blank = True,
        related_name="teams",
        #limit_choices_to = limit_choices
        )

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")
        # ordering = ("user",)
 
    def __str__(self):
        return self.name

    @property
    def team_size(self):
        return self.dancers.count()

    @property
    def size_limit(self):
        if level=='T':
            return 15
        else:
            return float('inf')

    @property
    def reached_limit(self):
        return (self.team_size > self.size_limit)

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

