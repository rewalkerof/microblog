from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return self.content[:100]

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-timestamp']
