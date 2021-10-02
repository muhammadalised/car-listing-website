from django.contrib import admin
from django.utils.html import format_html

from .models import Team

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(f"<img src='{object.photo.url}' style='border-radius:50%;' width='40'/>")

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)
    list_filter = ('designation',)

    search_fields = ('first_name', 'last_name', 'designation')

admin.site.register(Team, TeamAdmin)