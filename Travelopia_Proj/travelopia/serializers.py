from .models import *
from drf_queryfields import QueryFieldsMixin
from rest_framework import serializers


class LocationSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']


class TravellerSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    location = LocationSerializers(many=False)

    class Meta:
        model = Traveller
        fields = ['id', 'name', 'email', 'location', 'num_of_travellers', 'budget_per_person']


class TravellerPostSerializers(QueryFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Traveller
        fields = ['name', 'email', 'location', 'num_of_travellers', 'budget_per_person']
