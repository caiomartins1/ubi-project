from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ContentSibling
from api.serializers import ContentSiblingSerializer

from core.tests.test_models import sample_client, sample_content


CONTENT_SIBLINGS_URL = reverse('api:contentsibling-list')


def detail_url(content_sibling_uuid):
    """Return ContentSibling detail url"""
    return reverse(
        'api:contentsibling-detail',
        args=[content_sibling_uuid],
    )


class ContentSiblingTest(TestCase):
    """Test the ContentSibling API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_content_siblings_api(self):
        """Test retrieving a list of content siblings"""
        client = sample_client()
        parent = sample_content(client)
        content = sample_content(client, 'Torre de belem 2', 'descriçao 2')
        content2 = sample_content(client, 'Torre de belem 3', 'descriçao 3')
        ContentSibling.objects.create(
            parent=parent,
            content=content
        )
        ContentSibling.objects.create(
            parent=parent,
            content=content2
        )

        res = self.client.get(CONTENT_SIBLINGS_URL)
        content_siblings = ContentSibling.objects.all()
        serializer = ContentSiblingSerializer(content_siblings, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_content_sibling_detail(self):
        """Test viewing a content sibling detail"""
        client = sample_client()
        parent = sample_content(client)
        content = sample_content(client, 'Example', 'Example description')

        content_sibling = ContentSibling.objects.create(
            parent=parent,
            content=content,
        )

        url = detail_url(content_sibling.uuid)
        res = self.client.get(url)
        serializer = ContentSiblingSerializer(content_sibling)
        self.assertEqual(res.data, serializer.data)

    def test_create_content_sibling(self):
        """Test creating a content sibling"""
        client = sample_client()
        parent = sample_content(client)
        content = sample_content(
            client,
            'Example location',
            'Example description'
        )
        payload = {
            'parent': parent.uuid,
            'content': content.uuid
        }

        res = self.client.post(CONTENT_SIBLINGS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        content_sibling = ContentSibling.objects.get(uuid=res.data['uuid'])

        self.assertEqual(res.data['parent'], content_sibling.parent.uuid)
        self.assertEqual(res.data['content'], content_sibling.content.uuid)
