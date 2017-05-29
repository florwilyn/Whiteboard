from __future__ import unicode_literals

from django.contrib import admin

from .models import Users


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username']


admin.site.register(Users, UserProfileAdmin)