from django.test import TestCase
from django.utils import timezone
from core.models import Client, Content, ContentHighlight
import datetime


def sample_client(name='Test Client', nickname='TestClient'):
    return Client.objects.create(name=name, nickname=nickname)


def sample_content(client, title='Torre de belém',
                   description='Famous location in Lisbon.'):
    return Content.objects.create(
        client=client,
        title=title,
        description=description
    )


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
        """Test the Content string representation"""
        client = sample_client()
        title = 'Torre de belém'
        description = 'Famous location in Lisbon.'

        content = Content.objects.create(
            client=client,
            title=title,
            description=description
        )

        expected_string = content.title
        self.assertEqual(expected_string, str(content))

    def test_content_highlight_string_representation(self):
        """Test the ContentHighlight string representation"""
        client = sample_client()
        content = sample_content(client)

        content_highlight = ContentHighlight.objects.create(
            client=client,
            content=content,
        )

        expected = f'{content} Content Highlight'

        self.assertEqual(expected, str(content_highlight))
