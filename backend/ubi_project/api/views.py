from rest_framework import viewsets, mixins

from core.models import Client, Content, ContentHighlight, ContentSibling, \
                        ContentUpselling, ContentCard, HighlightCard, \
                        UpsellingCard

from api import serializers


class ClientViewSet(viewsets.ModelViewSet):
    """Manage clients in the database"""
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all client objects"""
        return self.queryset.all()

    def perform_create(self, serializer):
        """Create a new client"""
        serializer.save()


class ContentViewSet(viewsets.ModelViewSet):
    """Manage contents in the database"""
    serializer_class = serializers.ContentSerializer
    queryset = Content.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all content objects"""
        return self.queryset.all()


class ContentHighlightViewSet(viewsets.ModelViewSet):
    """Manage content highlights in the database"""
    serializer_class = serializers.ContentHighlightSerializer
    queryset = ContentHighlight.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all content highlight objects"""
        return self.queryset.all()


class ContentSiblingViewSet(viewsets.ModelViewSet):
    """Manage content siblings in the database"""
    serializer_class = serializers.ContentSiblingSerializer
    queryset = ContentSibling.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all content sibling objects"""
        return self.queryset.all()


class ContentUpsellingViewSet(viewsets.ModelViewSet):
    """Manage content upselling in the database"""
    serializer_class = serializers.ContentUpsellingSerializer
    queryset = ContentUpselling.objects.all()
    lookup_field = 'uuid'

    def get_queryset(self):
        """Return all content upselling objects"""
        return self.queryset.all()



class BaseCardAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Base viewset for cards attributes"""
    def get_queryset(self):
        """Return all ContentCard objects"""
        return self.queryset.all()


class ContentCardViewSet(BaseCardAttrViewSet):
    """List Content Cards"""
    queryset = ContentCard.objects.all()
    serializer_class = serializers.ContentCardSerializer


class UpsellingCardViewSet(BaseCardAttrViewSet):
    """List Content Cards"""
    queryset = UpsellingCard.objects.all()
    serializer_class = serializers.UpsellingCardSerializer


class HighlightCardViewSet(BaseCardAttrViewSet):
    """List Content Cards"""
    queryset = HighlightCard.objects.all()
    serializer_class = serializers.HighlightCardSerializer
