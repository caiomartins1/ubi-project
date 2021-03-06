from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets, mixins, status

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

    def get_queryset(self):
        """Return all content objects"""
        return self.queryset.all()

    def get_serializer_class(self):
        """Return apropried serializer class"""
        if self.action == 'upload_image':
            return serializers.ContentImageSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a content"""
        content = self.get_object()
        serializer = self.get_serializer(
            content,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


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
