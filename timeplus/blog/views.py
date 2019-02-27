from django.shortcuts import render,get_object_or_404

# Create your views here.

from . import models

def blog_summary(request):
    blogs = models.BlogArticles.objects.all()
    return render(request, 'blog/summary.html', {'blogs' : blogs})

def blog_article(request, article_id):
    article = get_object_or_404(models.BlogArticles, id=article_id)
    return render(request, 'blog/article.html', {'article' : article})

