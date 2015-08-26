from django.contrib import admin

# Register your models here.

from . import models
 
@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ["user__username"]

@admin.register(models.Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("org_name", "admin_name")
    search_fields = ["user__username"]