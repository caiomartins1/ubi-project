from rest_framework import viewsets, mixins

from core.models import Client
from api import serializers


class ClientViewSet(viewsets.ModelViewSet):
    """Manage clients in the database"""
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all client objects"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new client"""
        serializer.save()
