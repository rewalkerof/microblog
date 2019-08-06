from django.db import models
from django.conf import settings
from django.urls import reverse

from django.contrib.contenttypes.models import ContentType

from comments.models import Comment


def upload_location(instance, filename):
    return f'images/{instance}/{filename}'


def get_full_name(request):
    instance = request.user
    return f'{instance.email}\n{instance.first_name} {instance.last_name}'


class ActivePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(draft=False)


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field="width_field",
                              height_field="height_field")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = models.Manager()
    active = ActivePostManager()

    def get_full_name(self):
        instance = self.user
        return f'{instance.first_name} {instance.last_name}'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:list')

    def get_success_url(self):
        return reverse('posts:detail', kwargs={'id': self.id})

    class Meta:
        db_table = 'post'
        app_label = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-timestamp']

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
