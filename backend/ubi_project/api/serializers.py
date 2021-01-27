from rest_framework import serializers
from core.models import Client, Content, ContentHighlight, \
                        ContentSibling, ContentUpselling,  \
                        ContentCard, HighlightCard, UpsellingCard

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
        fields = ('uuid', 'client', 'title', 'description', 'country', 'city', 'latitude', 'longitude', 'image', 'image_02', 'image_03')
        read_only_fields = ('uuid',)


class ContentImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to contents"""

    class Meta:
        model = Content
        fields = ('uuid', 'image')
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


class ContentUpsellingSerializer(serializers.ModelSerializer):
    """Serializer for the ContentUpselling objects"""

    class Meta:
        model = ContentUpselling
        fields = '__all__'
        read_only_fields = ('uuid',)


class ContentCardSerializer(serializers.ModelSerializer):
    """Serializer for the ContentCard objects"""

    class Meta:
        model = ContentCard
        fields = '__all__'


class HighlightCardSerializer(serializers.ModelSerializer):
    """Serializer for the HighlightCard objects"""

    class Meta:
        model = HighlightCard
        fields = '__all__'


class UpsellingCardSerializer(serializers.ModelSerializer):
    """Serializer for the HighlightCard objects"""

    class Meta:
        model = UpsellingCard
        fields = '__all__'
