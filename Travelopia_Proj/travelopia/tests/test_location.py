from django.test import TestCase
from rest_framework import status

from ..models import Location
from ..serializers import LocationSerializers

from django.test import Client
client = Client()


class LocationTest(TestCase):
    """ Test module for Location model """

    def setUp(self):
        Location.objects.create(name='India')
        Location.objects.create(name='Europe')

    def test_location(self):
        location_india = Location.objects.get(name='India')
        location_europe = Location.objects.get(name='Europe')

        self.assertEqual(location_india.get_location(), "India is present.")
        self.assertEqual(location_europe.get_location(), "Europe is present.")


class GetAllLocationsTest(TestCase):
    """ Test module for GET all locations API """

    def setUp(self):
        Location.objects.create(name='India')
        Location.objects.create(name='Europe')
        Location.objects.create(name='Africa')
        Location.objects.create(name='Paris')

    def test_get_all_location(self):
        # get API response
        response = client.get('/api/location/')

        # get data from db
        location = Location.objects.all()
        serializer = LocationSerializers(location, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
