from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Content, Client
from api.serializers import ContentSerializer


CONTENTS_URL = reverse('api:content-list')

def sample_client(name='Test Client', nickname='TestClient'):
    return Client.objects.create(name=name, nickname=nickname)

def sample_content(client, title='Torre de belém', 
                   description='Famous location in Lisbon.'):
    return Content.objects.create(client=client, title=title, description=description)



def detail_url(content_uuid):
    """Return content detail URL"""
    return reverse('api:content-detail', args=[content_uuid])


class ContentsApiTests(TestCase):
    """Test the contents API"""

    def setUp(self):
        self.client = APIClient()
    
    def test_retrieve_contents_api(self):
        """Test retrieving a list of contents"""
        client = sample_client()
        content1 = sample_content(client)
        content2 = sample_content(client, title='Mosteiro1', description='Mosteiro description')

        res = self.client.get(CONTENTS_URL)

        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_content_detail(self):
        """Test viewing a content detail"""
        client = sample_client()
        content = sample_content(client)

        url = detail_url(content.uuid)
        res = self.client.get(url)

        serializer = ContentSerializer(content)
        self.assertEqual(res.data, serializer.data)

    def test_create_client(self):
        """Test creating a content"""
        client = sample_client()
        payload = {
            'client': client.uuid,
            'title': 'Spot 1',
            'description': 'Spot 1 description',
        }
        res = self.client.post(CONTENTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        content = Content.objects.get(uuid=res.data['uuid'])

        self.assertEqual(res.data['client'], client.uuid)
        self.assertEqual(res.data['title'], client.uuid)
        self.assertEqual(res.data['client'], client.uuid)

