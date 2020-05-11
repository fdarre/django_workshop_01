from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Restaurant

"""
The Restaurant model contains a GeoDjango field
It's necessary to use the OSMGeoAdmin class.
"""


@admin.register(Restaurant)
class RestaurantAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
