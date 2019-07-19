from django.urls import path
from django.contrib import admin
from .views import (post_create, post_delete, post_detail, post_list, post_edit)

admin.site.site_header = 'Тот еще секс'
admin.site.site_title = 'Тот еще секс'
admin.site.index_title = 'Тот еще секс'

app_name = 'posts'
urlpatterns = [

    path('', post_list, name="list"),
    path('create/', post_create, name="create"),
    path('<int:id>/detail', post_detail, name="detail"),
    path('<int:id>/edit/', post_edit, name="edit"),
    path('delete/', post_delete, name="delete"),
]
