from django.contrib import admin

# Register your models here.
from .models import *


class feedbackAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'emailId', 'phoneNumber', 'messageDate')

admin.site.register(feedback, feedbackAdmin)

class projectAdmin(admin.ModelAdmin):
    list_display = ('projectName', 'projectLink')

admin.site.register(projects, projectAdmin)