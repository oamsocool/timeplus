from django.contrib import admin
from django.urls import path,re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_summary, name = 'blog_summary'),
    re_path('(?P<article_id>\d)/', views.blog_article, name = 'blog_article'),
]
