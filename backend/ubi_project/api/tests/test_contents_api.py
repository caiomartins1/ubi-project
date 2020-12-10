from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Content
from core.tests.test_models import sample_content, sample_client
from api.serializers import ContentSerializer


CONTENTS_URL = reverse('api:content-list')


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
        sample_content(client)
        sample_content(client,
                       title='Mosteiro1',
                       description='Mosteiro description')

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

    def test_create_content(self):
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

        self.assertEqual(res.data['client'], content.client.uuid)
        self.assertEqual(res.data['title'], content.title)
        self.assertEqual(res.data['description'], content.description)
