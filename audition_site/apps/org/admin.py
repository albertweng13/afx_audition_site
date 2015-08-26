from django.contrib import admin

# Register your models here.

from . import models
 
@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "team")
    search_fields = ["user__username"]

@admin.register(models.Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("org_name", "admin_name", "choosingProjects", "allSet")#, #"castingGroups")
    search_fields = ["user__username"]

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "allSet")
    search_fields = ["user__username"]

@admin.register(models.CastingGroup)
class CGAdmin(admin.ModelAdmin):
    list_display = ("org", "video_link")
    search_fields = ["user__username"]

@admin.register(models.Dancer)
class DancerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "org", "casting_group", "numClaims", "eligible", "eligibleTraining", "allSet")
    search_fields = ["user__username"]
