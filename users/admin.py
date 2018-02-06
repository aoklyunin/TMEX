# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from tmex.admin import SubmissionInline
from users.models import ScUser


class ScUserAdmin(admin.ModelAdmin):
    inlines = [
        SubmissionInline,
    ]

admin.site.register(ScUser, ScUserAdmin)
