from django.contrib import admin
from .models import Team, Person, Membership


# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ["person", "team"]
