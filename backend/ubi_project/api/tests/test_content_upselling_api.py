from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ContentUpselling
from api.serializers import ContentUpsellingSerializer

from core.tests.test_models import sample_client, sample_content


CONTENT_UPSELLING_URL = reverse('api:contentupselling-list')


def detail_url(content_upselling_uuid):
    """Return ContentUpselling detail URL"""
    return reverse(
        'api:contentupselling-detail',
        args=[content_upselling_uuid],
    )


class ContentUpsellingTest(TestCase):
    """Test the ContentUpselling API"""

    def setUp(self):
        self.api_client = APIClient()
        self.client = sample_client()
        self.content = sample_content(self.client)

    def test_retrieve_content_upselling_api(self):
        """Test retrieving a list of ContentUpselling"""
        ContentUpselling.objects.create(
            client=self.client,
            content=self.content,
            title='ContentUpselling1'
        )
        ContentUpselling.objects.create(
            client=self.client,
            content=sample_content(
                client=self.client,
                title="Praia 1",
                description="A melhor praia"
            ),
            title='ContentUpselling2'
        )

        res = self.api_client.get(CONTENT_UPSELLING_URL)
        content_upselling = ContentUpselling.objects.all()
        serializer = ContentUpsellingSerializer(content_upselling, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_content_upselling_detail(self):
        """Test viewing a content upselling detail"""
        content_upselling = ContentUpselling.objects.create(
            client=self.client,
            content=self.content,
            title='ContentUpselling1'
        )

        url = detail_url(content_upselling.uuid)
        res = self.api_client.get(url)
        serializer = ContentUpsellingSerializer(content_upselling)
        self.assertEqual(res.data, serializer.data)

    def test_create_content_upselling(self):
        """Test creating a new content upselling object"""
        payload = {
            'client': self.client.uuid,
            'content': self.content.uuid,
            'title': 'ContentUpselling 1',
        }

        res = self.api_client.post(CONTENT_UPSELLING_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        content_upselling = ContentUpselling.objects.get(uuid=res.data['uuid'])

        self.assertEqual(res.data['client'], content_upselling.client.uuid)
        self.assertEqual(res.data['content'], content_upselling.content.uuid)
        self.assertEqual(res.data['title'], content_upselling.title)
