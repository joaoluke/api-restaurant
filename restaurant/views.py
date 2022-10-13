from rest_framework import generics
from restaurant.models import Plate
from restaurant.serializers import PlateSerializer

class PlateListView(generics.ListAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer