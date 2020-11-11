from django.contrib import admin
from .models import BookingTransaction, Message, Rating

admin.site.register(Message)
admin.site.register(Rating)
admin.site.register(BookingTransaction)

# Register your models here.
