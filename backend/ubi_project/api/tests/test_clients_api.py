from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Client
from api.serializers import ClientSerializer


CLIENTS_URL = reverse('api:client-list')


def detail_url(client_uuid):
    """Return client detail URL"""
    return reverse('api:client-detail', args=[client_uuid])


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

    def test_view_client_detail(self):
        """Test viewing a client detail"""
        client = Client.objects.create(
            name='Test User',
            nickname='TestUser1'
        )
        url = detail_url(client.uuid)
        res = self.client.get(url)

        serializer = ClientSerializer(client)
        self.assertEqual(res.data, serializer.data)

    def test_create_client(self):
        """Test creating a client"""
        payload = {
            'name': 'Test User',
            'nickname': 'testuser1',
        }
        res = self.client.post(CLIENTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        client = Client.objects.get(uuid=res.data['uuid'])

        for key in payload.keys():
            self.assertEqual(payload[key], getattr(client, key))
