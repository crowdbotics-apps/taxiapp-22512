from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BookingTransactionViewSet, MessageViewSet, RatingViewSet

router = DefaultRouter()
router.register("message", MessageViewSet)
router.register("rating", RatingViewSet)
router.register("bookingtransaction", BookingTransactionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
