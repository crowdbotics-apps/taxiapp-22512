from django.contrib import admin
from .models import Vehicle, VehicleType

admin.site.register(VehicleType)
admin.site.register(Vehicle)

# Register your models here.
