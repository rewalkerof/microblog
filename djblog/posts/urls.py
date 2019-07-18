from django.urls import path
from django.contrib import admin
from . import views


admin.site.site_header = 'Тот еще секс'
admin.site.site_title = 'Тот еще секс'
admin.site.index_title = 'Тот еще секс'

urlpatterns = [
    path('', views.post_home, name="post_home"),
    path('create/', views.post_create, name="post_create"),
    path('detail', views.post_detail, name="post_detail"),
    path('list', views.post_list, name="post_list"),
    path('update', views.post_update, name="post_update"),
    path('delete', views.post_delete, name="post_delete"),
]
