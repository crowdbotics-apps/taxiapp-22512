from django.contrib import admin
from .models import UserWallet, PaymentMethod, DriverWallet

admin.site.register(UserWallet)
admin.site.register(PaymentMethod)
admin.site.register(DriverWallet)

# Register your models here.
