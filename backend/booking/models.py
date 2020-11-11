from django.conf import settings
from django.db import models


class Message(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        on_delete=models.CASCADE,
        related_name="message_user",
    )
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        on_delete=models.CASCADE,
        related_name="message_driver",
    )
    message = models.TextField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    booking = models.ForeignKey(
        "booking.BookingTransaction",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="message_booking",
    )


class Rating(models.Model):
    "Generated Model"
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        on_delete=models.CASCADE,
        related_name="rating_driver",
    )
    rating = models.FloatField()
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rating_user",
    )
    review = models.TextField(
        null=True,
        blank=True,
    )


class BookingTransaction(models.Model):
    "Generated Model"
    distance = models.FloatField()
    price = models.FloatField()
    status = models.CharField(
        max_length=10,
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    timestamp_depart = models.DateTimeField()
    timestamp_arrive = models.DateTimeField()
    user = models.ForeignKey(
        "taxi_profile.UserProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_user",
    )
    driver = models.ForeignKey(
        "taxi_profile.DriverProfile",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_driver",
    )
    pickup = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_pickup",
    )
    dropoff = models.ForeignKey(
        "location.MapLocation",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="bookingtransaction_dropoff",
    )
    tip = models.FloatField(
        null=True,
        blank=True,
    )


# Create your models here.
