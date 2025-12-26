from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, Category

def home(request):
    articles = NewsArticle.objects.all().order_by('-published_at')
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)

    context = {
        'article': article
    }
    return render(request, 'detail.html', context)
