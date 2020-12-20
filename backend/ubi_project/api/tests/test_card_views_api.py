from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ContentCard, HighlightCard, UpsellingCard, \
                        ContentUpselling, ContentHighlight

from api.serializers import ContentCardSerializer, HighlightCardSerializer, \
                            UpsellingCardSerializer

from core.tests.test_models import sample_client, sample_content

CONTENT_CARD_URL = reverse('api:contentcard-list')


HIGHLIGHT_CARD_URL = reverse('api:highlightcard-list')


UPSELLING_CARD_URL = reverse('api:upsellingcard-list')


class CardsApiTests(TestCase):
    """Test the card views api"""

    def setUp(self):
        self.client =  APIClient()
    
    def test_retrieve_content_card_list(self):
        """Test retrieving a list of content cards"""
        client = sample_client()
        sample_content(client)
        sample_content(
            client=client,
            title="Torre 2",
            description="description torre 2"
        )

        res = self.client.get(CONTENT_CARD_URL)
        content_cards = ContentCard.objects.all()
        serializer = ContentCardSerializer(content_cards, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_retrieve_upselling_card_list(self):
        """Test retrieving a list of upselling cards"""
        client = sample_client()
        content = sample_content(client)
        
        ContentUpselling.objects.create(
            client=client,
            content=content,
            title='ContentUpselling1'
        )

        ContentUpselling.objects.create(
            client=client,
            content=sample_content(
                client=client,
                title="Praia 1",
                description="A melhor praia"
            ),
            title='ContentUpselling2'
        )

        res = self.client.get(UPSELLING_CARD_URL)
        upselling_cards = UpsellingCard.objects.all()
        serializer = UpsellingCardSerializer(upselling_cards, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_highlight_card_list(self):
        """Test retrieving a list of highlight cards"""
        client = sample_client()
        content = sample_content(client)
        
        ContentHighlight.objects.create(
            client=client,
            content=content,
        )

        ContentHighlight.objects.create(
            client=client,
            content=sample_content(
                client=client,
                title="Torre de belem 2",
                description="description Torre de belem 2",
            )
        )

        res = self.client.get(HIGHLIGHT_CARD_URL)
        highlight_card = HighlightCard.objects.all()
        serializer = HighlightCardSerializer(highlight_card, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

