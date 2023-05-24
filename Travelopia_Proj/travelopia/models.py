from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '%s is added.' % self.name

    def get_location(self):
        return '%s is present.' % self.name

    class Meta:
        db_table = "location"
        ordering = ['name']


class Traveller(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=100)
    location = models.ForeignKey(Location, related_name='travel_location', on_delete=models.CASCADE)
    num_of_travellers = models.IntegerField()
    budget_per_person = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return '%s is added.' % self.email

    def get_email(self):
        return 'account with %s is present.' % self.email

    class Meta:
        db_table = "traveller"
        ordering = ['name']
