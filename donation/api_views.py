from rest_framework import generics
from .models import Donation
from .serializers import DonationSerializer

class DonationListCreate(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

class DonationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
