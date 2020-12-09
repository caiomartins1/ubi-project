from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ContentHighlight
from api.serializers import ContentHighlightSerializer

from core.tests.test_models import sample_client, sample_content

import datetime


CONTENT_HIGHLIGHTS_URL = reverse('api:contenthighlight-list')


def detail_url(content_highlight_uuid):
    """Return ContentHighlight detail url"""
    return reverse(
        'api:contenthighlight-detail',
        args=[content_highlight_uuid],
    )


class ContentHighlightsTest(TestCase):
    """Test the ContentHighlights API"""

    def setUp(self):
        self.api_client = APIClient()
        self.client = sample_client()
        self.content = sample_content(self.client)

    def test_retrieve_content_highlights_api(self):
        """Test retrieving a list of ContentHighlights"""
        ContentHighlight.objects.create(
            client=self.client,
            content=sample_content(
                client=self.client,
                title="Torre de belem 1",
                description="description Torre de belem 1",
            )
        )
        ContentHighlight.objects.create(
            client=self.client,
            content=sample_content(
                client=self.client,
                title="Torre de belem 2",
                description="description Torre de belem 2",
            )
        )

        res = self.api_client.get(CONTENT_HIGHLIGHTS_URL)
        content_highlights = ContentHighlight.objects.all()
        serializer = ContentHighlightSerializer(content_highlights, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_content_highlight_detail(self):
        """Test viewing a content highlight detail"""
        content_highlight = ContentHighlight.objects.create(
            client=self.client,
            content=self.content,
        )

        url = detail_url(content_highlight.uuid)
        res = self.api_client.get(url)
        serializer = ContentHighlightSerializer(content_highlight)
        self.assertEqual(res.data, serializer.data)

    def test_create_content_highlight(self):
        """Test creating a content highlight"""
        payload = {
            'client': self.client.uuid,
            'content': self.content.uuid,
            'is_always': False,
            'start_date': datetime.date(1999, 8, 25),
            'end_date': datetime.date(1999, 9, 1)
        }

        res = self.api_client.post(CONTENT_HIGHLIGHTS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        content_highlight = ContentHighlight.objects.get(uuid=res.data['uuid'])

        self.assertEqual(res.data['client'], content_highlight.client.uuid)
        self.assertEqual(res.data['content'], content_highlight.content.uuid)
        self.assertEqual(res.data['is_always'], content_highlight.is_always)
        self.assertEqual(
            res.data['start_date'],
            str(content_highlight.start_date)
        )
        self.assertEqual(res.data['end_date'], str(content_highlight.end_date))
