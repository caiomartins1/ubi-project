from rest_framework import viewsets

from core.models import Client, Content
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

class ContentViewSet(viewsets.ModelViewSet):
    """Manage contents in the database"""
    serializer_class = serializers.ContentSerializer
    queryset = Content.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all content objects"""
        return self.queryset.all()
    
