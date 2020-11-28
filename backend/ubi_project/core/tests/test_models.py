from django.test import TestCase
from django.utils import timezone
from core.models import Client
import datetime
import uuid


class ClientModelTest(TestCase):
    """Tests suites for the Client Model"""
    def test_create_client__sucessfull(self):
        """Test creating a new client successfull"""
        name = 'Caio Martins'
        nickname = 'caiomartins'
        registration_date = timezone.now()

        client = Client.objects.create(
            name=name,
            nickname=nickname,
            registration_date=registration_date
        )

        self.assertEqual(client.name, name)
        self.assertEqual(client.nickname, nickname)
        self.assertTrue(isinstance(client.registration_date, datetime.date))

    def test_client_logo_returns_expected_string(self):
        name = 'Caio Martins'
        nickname = 'caiomartins'
        registration_date = timezone.now()

        client = Client.objects.create(
            name=name,
            nickname=nickname,
            registration_date=registration_date
        )
        expected_string = 'media/{}/logo.png'.format(client.id)

        self.assertEqual(expected_string, client.client_logo)
    
    def test_client_str_representation(self):
        name = 'Caio Martins'
        nickname = 'caiomartins'
        registration_date = timezone.now()

        client = Client.objects.create(
            name=name,
            nickname=nickname,
            registration_date=registration_date
        )

        self.assertEqual(name, str(client))







