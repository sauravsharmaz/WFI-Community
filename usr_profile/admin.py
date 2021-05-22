from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth import models
from usr_profile.models import proFile

# Register your models here.
@admin.register(proFile)
class proFileAdmin(admin.ModelAdmin):
    list_display= ['usr']
