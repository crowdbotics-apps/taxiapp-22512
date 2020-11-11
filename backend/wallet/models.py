from django.conf import settings
from django.db import models


class UserWallet(models.Model):
    "Generated Model"
    user = models.OneToOneField(
        "taxi_profile.UserProfile",
        on_delete=models.CASCADE,
        related_name="userwallet_user",
    )
    balance = models.FloatField()
    expiration_date = models.DateTimeField()


class PaymentMethod(models.Model):
    "Generated Model"
    wallet = models.ForeignKey(
        "wallet.UserWallet",
        on_delete=models.CASCADE,
        related_name="paymentmethod_wallet",
    )
    account_token = models.CharField(
        max_length=255,
    )
    payment_account = models.CharField(
        max_length=10,
    )
    timestamp_created = models.DateTimeField(
        auto_now_add=True,
    )


class DriverWallet(models.Model):
    "Generated Model"
    driver = models.OneToOneField(
        "taxi_profile.DriverProfile",
        on_delete=models.CASCADE,
        related_name="driverwallet_driver",
    )
    balance = models.FloatField()
    expiration_date = models.DateTimeField()


# Create your models here.
