from rest_framework.generics import ListAPIView

from posts.models import Post
from .serializer import PostSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
