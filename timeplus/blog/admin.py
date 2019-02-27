from django.contrib import admin

# Register your models here.

from blog.models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("author", "publish")
    search_fields = ['title', 'body']
    raw_id_fields = ("author",)
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)
