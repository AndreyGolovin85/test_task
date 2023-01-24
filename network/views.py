from django_filters import filters
from rest_framework import viewsets

from network.models import Network
from network.serializers import NetworkSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']
