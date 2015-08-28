from django.contrib import admin

# Register your models here.

from . import models
 
@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "team")
    search_fields = ["user__username"]

@admin.register(models.Semester)
class SemAdmin(admin.ModelAdmin):
    list_display = ("admin_name", "choosingProjects", "allSet")#, #"castingGroups")
    search_fields = ["user__username"]

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "allSet")
    search_fields = ["user__username"]

@admin.register(models.CastingGroup)
class CGAdmin(admin.ModelAdmin):
    list_display = ("semester", "video_link", "dancer_ids")
    search_fields = ["user__username"]

@admin.register(models.Dancer)
class DancerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "semester", "casting_group", "numClaims", "eligible", "eligibleTraining", "allSet")
    search_fields = ["user__username"]
