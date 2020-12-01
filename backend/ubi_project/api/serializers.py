from rest_framework import serializers
from core.models import Client

# TODO: define camps for list and detailed views, countrycamp not serializable, 


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for client objects"""

    class Meta:
        model = Client
        fields = ('uuid', 'name', 'nickname',)
        read_only_fields = ('uuid',)
