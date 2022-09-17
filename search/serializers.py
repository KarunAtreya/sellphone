
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import PhoneDocument

class PhoneDocumentSerializer(DocumentSerializer):
    """Serializer for the Phone document."""

    class Meta:
        """Meta options."""

        document = PhoneDocument

        fields = (
            'id',
            'user',
            'image1',
            'brand',
            'model',
            'price',
            
        )