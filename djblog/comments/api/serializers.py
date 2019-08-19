from rest_framework.serializers import (
    ModelSerializer,

    SerializerMethodField,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
    RelatedField,
)

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content_type',
            'object_id',
            'content',
        ]
