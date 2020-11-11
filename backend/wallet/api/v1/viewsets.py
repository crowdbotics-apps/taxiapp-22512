from rest_framework import authentication
from wallet.models import UserWallet, PaymentMethod, DriverWallet
from .serializers import (
    UserWalletSerializer,
    PaymentMethodSerializer,
    DriverWalletSerializer,
)
from rest_framework import viewsets


class UserWalletViewSet(viewsets.ModelViewSet):
    serializer_class = UserWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = UserWallet.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class DriverWalletViewSet(viewsets.ModelViewSet):
    serializer_class = DriverWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = DriverWallet.objects.all()
