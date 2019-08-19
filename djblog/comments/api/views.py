from comments.models import Comment
from rest_framework.generics import (
    RetrieveAPIView,
    ListCreateAPIView)

from .serializers import (
    CommentSerializer
)

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
