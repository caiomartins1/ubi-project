from rest_framework import viewsets, mixins

from core.models import Client
from api import serializers


class ClientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage clients in the database"""
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        """Return all client objects"""
        return self.queryset.all()
