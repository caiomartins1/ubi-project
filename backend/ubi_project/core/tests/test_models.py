from django.test import TestCase
from django.utils import timezone
from core.models import Client, Content
import datetime


def sample_client(name='Test Client', nickname='TestClient'):
    return Client.objects.create(name=name, nickname=nickname)


class ClientModelTest(TestCase):
    """Tests suites for the Client Model"""

    def test_create_client_sucessfull(self):
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
        """Test the returned client logo string is correct"""
        name = 'Caio Martins'
        nickname = 'caiomartins'
        registration_date = timezone.now()

        client = Client.objects.create(
            name=name,
            nickname=nickname,
            registration_date=registration_date
        )
        expected_string = 'media/{}/logo.png'.format(client.uuid)

        self.assertEqual(expected_string, client.client_logo)

    def test_client_str_representation(self):
        """Test the string representation of a client"""
        name = 'Caio Martins'
        nickname = 'caiomartins'
        registration_date = timezone.now()

        client = Client.objects.create(
            name=name,
            nickname=nickname,
            registration_date=registration_date
        )

        self.assertEqual(name, str(client))

    def test_create_content_successfull(self):
        """Test creating a content object"""
        client = sample_client()
        title = 'Torre de belém'
        description = 'Famous location in Lisbon.'
        
        content = Content.objects.create(
            client=client,
            title=title,
            description=description
        )

        self.assertEqual(content.client.uuid, client.uuid)
        self.assertEqual(content.title, title)
        self.assertEqual(content.description, description)

    def test_content_string_representation(self):
        """Test the content string representation"""
        client = sample_client()
        title = 'Torre de belém'
        description = 'Famous location in Lisbon.'

        content = Content.objects.create(
            client=client,
            title=title,
            description=description
        )
        
        expected_string = content.title
        self.assertEqual(content.title, expected_string)
        