from django.contrib import admin
from django.utils.html import format_html
from .models import Car

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f"<img src='{object.car_photo.url}' style='border-radius:50%;' width='40'/>")

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title',)
    list_editable = ('is_featured',)
    list_filter = ('city', 'model', 'body_style', 'fuel_type')
    search_fields = ('id', 'car_title', 'city', 'model', 'body_type', 'fuel_type')

admin.site.register(Car, CarAdmin)
