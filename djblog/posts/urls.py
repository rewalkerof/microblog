from django.urls import path
from django.contrib import admin
from .views import (post_create, post_delete, post_detail, post_list, post_update)

admin.site.site_header = 'Тот еще секс'
admin.site.site_title = 'Тот еще секс'
admin.site.index_title = 'Тот еще секс'

app_name = 'posts'
urlpatterns = [

    path('', post_list, name="post_list"),
    path('create/', post_create, name="post_create"),
    path('detail/<int:id>/', post_detail, name="detail"),
    path('update/', post_update, name="post_update"),
    path('delete/', post_delete, name="post_delete"),
]
