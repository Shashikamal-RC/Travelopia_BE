from django.test import TestCase
from rest_framework import status

from ..models import Traveller, Location
from ..serializers import TravellerSerializers, TravellerPostSerializers

from django.test import Client
client = Client()


class TravellerTest(TestCase):
    """ Test module for Traveller model """

    def setUp(self):
        location = Location.objects.create(name='India')
        Traveller.objects.create(name='john', email="john@gmail.com", location=location, num_of_travellers=5, budget_per_person=100)
        Traveller.objects.create(name='steve', email="steve@gmail.com", location=location, num_of_travellers=15, budget_per_person=200)

    def test_traveller_account(self):
        john = Traveller.objects.get(email="john@gmail.com")
        steve = Traveller.objects.get(email="steve@gmail.com")

        self.assertEqual(john.get_email(), "account with john@gmail.com is present.")
        self.assertEqual(steve.get_email(), "account with steve@gmail.com is present.")


class GetAllTravellersTest(TestCase):
    """ Test module for GET all Travellers API """

    def setUp(self):
        location = Location.objects.create(name='India')
        Traveller.objects.create(name='john', email="john@gmail.com", location=location, num_of_travellers=35, budget_per_person=100)
        Traveller.objects.create(name='steve', email="steve@gmail.com", location=location, num_of_travellers=15, budget_per_person=200)

    def test_get_all_travellers(self):
        # get API response
        response = client.get('/api/traveller/')

        # get data from db
        traveller = Traveller.objects.all()
        serializer = TravellerSerializers(traveller, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
