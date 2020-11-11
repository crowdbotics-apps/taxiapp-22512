from rest_framework import authentication
from vehicle.models import Vehicle, VehicleType
from .serializers import VehicleSerializer, VehicleTypeSerializer
from rest_framework import viewsets


class VehicleTypeViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleTypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = VehicleType.objects.all()


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vehicle.objects.all()
