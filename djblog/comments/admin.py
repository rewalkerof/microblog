from django.contrib import admin
from .models import Comment


# Register your models here.

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', "user", "content", "timestamp"]

    class Meta:
        model = Comment


admin.site.register(Comment, CommentsAdmin)
