from rest_framework.serializers import ModelSerializer

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
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'user',
            'timestamp',
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
