from rest_framework import authentication
from booking.models import BookingTransaction, Message, Rating
from .serializers import (
    BookingTransactionSerializer,
    MessageSerializer,
    RatingSerializer,
)
from rest_framework import viewsets


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Message.objects.all()


class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Rating.objects.all()


class BookingTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = BookingTransactionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = BookingTransaction.objects.all()
