from rest_framework import serializers
from core.models import Client, Content, ContentHighlight, ContentSibling

# TODO: define camps for list and detailed views, countrycamp not serializable


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client objects"""

    class Meta:
        model = Client
        fields = ('uuid', 'name', 'nickname',)
        read_only_fields = ('uuid',)


class ContentSerializer(serializers.ModelSerializer):
    """Serializer for the content objects"""

    # title and image
    class Meta:
        model = Content
        fields = ('uuid', 'client', 'title', 'description',)
        read_only_fields = ('uuid',)


class ContentHighlightSerializer(serializers.ModelSerializer):
    """Serializer for the ContentHighlight objects"""

    class Meta:
        model = ContentHighlight
        fields = '__all__'
        read_only_fields = ('uuid',)


class ContentSiblingSerializer(serializers.ModelSerializer):
    """Serializer for the ContentSibling objects"""

    class Meta:
        model = ContentSibling
        fields = '__all__'
        read_only_fields = ('uuid',)
