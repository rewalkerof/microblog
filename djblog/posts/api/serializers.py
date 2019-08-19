from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField,
)

from comments.api.serializers import CommentSerializer
# from models import Comment
from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'user',
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class PostDetailSerializer(ModelSerializer):
    # comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'timestamp',
            'image',
            # 'comments',
        ]

    def get_image(self, obj):
        return obj.image.path

    # def get_comments(self, obj):
    #     content_type = obj.get_content_type
    #     obj_id = obj.id
    #     qs = Comment.objects.filter_by_instance(obj)
    #     comments = CommentSerializer(qs, many=True).data
    #     return comments


class PostListSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='id',
    )

    deleter = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='id'
    )
    username = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'username',
            'timestamp',
            'deleter',
        ]

    def get_username(self, obj):
        return obj.user.username
