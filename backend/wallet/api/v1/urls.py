from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserWalletViewSet, PaymentMethodViewSet, DriverWalletViewSet

router = DefaultRouter()
router.register("userwallet", UserWalletViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("driverwallet", DriverWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
