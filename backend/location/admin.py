from django.contrib import admin
from .models import VehicleLocation, ProfileLocation, MapLocation

admin.site.register(ProfileLocation)
admin.site.register(MapLocation)
admin.site.register(VehicleLocation)

# Register your models here.
