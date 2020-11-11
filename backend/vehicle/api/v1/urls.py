from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register("vehicletype", VehicleTypeViewSet)
router.register("vehicle", VehicleViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
