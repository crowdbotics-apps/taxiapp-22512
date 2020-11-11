from django.conf import settings
from django.db import models


class ProfileLocation(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "taxi_profile.UserProfile",
        on_delete=models.CASCADE,
        related_name="profilelocation_user",
    )
    latitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )
    longitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )


class MapLocation(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    latitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )
    longitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )


class VehicleLocation(models.Model):
    "Generated Model"
    vehicle = models.OneToOneField(
        "vehicle.Vehicle",
        on_delete=models.CASCADE,
        related_name="vehiclelocation_vehicle",
    )
    latitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )
    longitude = models.DecimalField(
        max_digits=12,
        decimal_places=8,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )


# Create your models here.
