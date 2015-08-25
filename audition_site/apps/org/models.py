from django.db import models

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
	SEMESTERS = (
		('Sp', 'Spring'),
		('Su', 'Summer'),
		('Fa', 'Fall')
	)
	name = models.CharField(max_length=50)
	semester = models.CharField(max_length=2, choices=SEMESTERS)

class Exec(models.Model):
	#Relations
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name="exec",
		verbose_name=_("user")
	)
	org = models.ForeignKey(
		Organization,
		related_name="execs",
		verbose_name=_("org")
		)
	ROLES = (
		#TODO: EXEC ROLES?
		)
	name = models.CharField(max_length=50)
	email = models.EmailField
	role = models.CharField(max_length=1, choices=ROLES)

class Director(models.Model):
	#Relations
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name="profile",
		verbose_name=_("user")
	)
	org = models.ForeignKey(
		Organization,
		related_name="directors",
		verbose_name=_("org")
		)
	organization = models.ForeignKey(models.ForeignKey(Organization))
	team = models.ForeignKey(models.ForeignKey(Team))
	#Attributes - Mandatory
	name = models.CharField(max_length=50)
	email = models.EmailField

class Team(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="teams",
		verbose_name=_("org")
		)
	name = models.CharField(max_length=50)

class ProjectTeam(Team):
	dancers = models.ManyToMany(
		Dancer,
		related_name="projects"
		verbose_name=_("dancers"))

class TrainingTeam(Team):
	dancers = models.ManyToMany(
		Dancer,
		related_name="training"
		verbose_name=_("dancers"))

class CastingGroup(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="castingGroups",
		verbose_name=_("org")
		)
	groupId = models.PositiveIntegerField
	videoLink = models.URLField

class Dancer(models.Model):
	org = models.ForeignKey(
		Organization,
		related_name="dancers",
		verbose_name=_("org")
		)
	castingGroup = models.ForeignKey(
		CastingGroup,
		related_name = "dancers",
		verbose_name=_("casting group"),
		blank=True
		)
	name = models.CharField(max_length=50)
	email = models.EmailField
	dancerId = models.PositiveIntegerField
	eligible = castingGroup != None
	eligibleTraining = eligible && projects.size < 2
	numClaims = models.PositiveIntegerField(
        default=0,
        verbose_name=_("interaction")
        )
	allSet = (!eligible && numClaims == 0) || (numClaims == 1 || numClaims == 2)



