from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="userprofile_user",
    )
    mobile_number = models.CharField(
        null=True,
        blank=True,
        max_length=20,
    )
    photo = models.URLField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )
    timestamp_created = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )
    last_login = models.DateTimeField(
        null=True,
        blank=True,
    )


class DriverProfile(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="driverprofile_user",
    )
    mobile_number = models.CharField(
        max_length=20,
    )
    photo = models.URLField()
    driver_status = models.CharField(
        max_length=50,
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )
    last_login = models.DateTimeField()


class Document(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="document_user",
    )
    file = models.URLField()
    description = models.TextField(
        null=True,
        blank=True,
    )


class InviteCode(models.Model):
    "Generated Model"
    code = models.CharField(
        max_length=20,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="invitecode_user",
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )


class Notification(models.Model):
    "Generated Model"
    type = models.CharField(
        max_length=20,
    )
    message = models.TextField()
    users = models.ManyToManyField(
        "users.User",
        related_name="notification_users",
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )


# Create your models here.
