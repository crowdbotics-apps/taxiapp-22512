from django.conf import settings
from django.db import models


class VehicleType(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    icon = models.URLField()
    base_rate = models.FloatField()


class Vehicle(models.Model):
    "Generated Model"
    type_description = models.CharField(
        max_length=255,
    )
    plate_number = models.CharField(
        max_length=10,
    )
    timestamp_registered = models.DateTimeField(
        auto_now_add=True,
    )
    vehicle_type = models.ForeignKey(
        "vehicle.VehicleType",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="vehicle_vehicle_type",
    )
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="vehicle_driver",
    )
    is_on_duty = models.BooleanField(
        null=True,
        blank=True,
    )


# Create your models here.
