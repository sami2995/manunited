from django.shortcuts import render, get_object_or_404
from .models import NewsArticle, Category
from .forms import ContactForm

def home(request):
    contact_success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            contact_success = True
            form = ContactForm()
    else:
        form = ContactForm()

    articles = NewsArticle.objects.all().order_by('-published_at')
    categories = Category.objects.all()

    context = {
        'articles': articles,
        'categories': categories,
        'contact_form': form,
        'contact_success': contact_success,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)

    context = {
        'article': article
    }
    return render(request, 'detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # show a success message in the template
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
