from django.contrib import admin

from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', "title", "updated", "timestamp"]
    list_display_links = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ['title']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
