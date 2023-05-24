from .models import *
from .serializers import *
from rest_framework import generics


class LocationViewSet(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers

    def get(self, request, *args, **kwargs):
        """
            A Set of projects belongs to a group called Project Cluster.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            A Set of projects belongs to a group called Project Cluster.
        """
        return self.create(request, *args, **kwargs)


class TravellerViewSet(generics.ListCreateAPIView):
    queryset = Traveller.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TravellerPostSerializers
        else:
            return TravellerSerializers

    def get(self, request, *args, **kwargs):
        """
            A Set of projects belongs to a group called Project Cluster.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            A Set of projects belongs to a group called Project Cluster.
        """
        return self.create(request, *args, **kwargs)
