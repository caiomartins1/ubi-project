from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Client
from api.serializers import ClientSerializer


CLIENTS_URL = reverse('api:client-list')


class ClientsApiTests(TestCase):
    """Test the client api"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_clients_list(self):
        """Test retrieving a list of clients"""
        Client.objects.create(
            name='Test User',
            nickname='TestUser1'
        )
        Client.objects.create(
            name='Test User 2',
            nickname='TestUser2'
        )

        res = self.client.get(CLIENTS_URL)

        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
