from rest_framework import serializers
from location.models import VehicleLocation, ProfileLocation, MapLocation


class ProfileLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileLocation
        fields = "__all__"


class MapLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapLocation
        fields = "__all__"


class VehicleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocation
        fields = "__all__"
