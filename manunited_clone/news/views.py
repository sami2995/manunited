from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import NewsArticle, Category, Comment, Contact
from .forms import ContactForm, CategoryForm, NewsArticleForm, CommentForm

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

    comment_success = False
    if request.method == 'POST':
        email = request.POST.get('user_email')
        comment_text = request.POST.get('user_comment')
        if email and comment_text:
            Comment.objects.create(article=article, email=email, comment=comment_text)
            comment_success = True

    comments = article.comments.all().order_by('-created_at')

    context = {
        'article': article,
        'comments': comments,
        'comment_success': comment_success,
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


### Custom CRUD for Category ###
def category_list(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'news/categories.html', {'categories': categories})


def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:category_list'))
    else:
        form = CategoryForm()
    return render(request, 'news/category_form.html', {'form': form, 'action': 'Add'})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:category_list'))
    else:
        form = CategoryForm(instance=category)
    return render(request, 'news/category_form.html', {'form': form, 'action': 'Edit'})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect(reverse('news:category_list'))
    return render(request, 'news/category_confirm_delete.html', {'category': category})


### CRUD for NewsArticle ###
def article_list(request):
    articles = NewsArticle.objects.all().order_by('-published_at')
    return render(request, 'news/articles.html', {'articles': articles})


def article_add(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:article_list'))
    else:
        form = NewsArticleForm()
    return render(request, 'news/article_form.html', {'form': form, 'action': 'Add'})


def article_edit(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:article_list'))
    else:
        form = NewsArticleForm(instance=article)
    return render(request, 'news/article_form.html', {'form': form, 'action': 'Edit'})


def article_delete(request, pk):
    article = get_object_or_404(NewsArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect(reverse('news:article_list'))
    return render(request, 'news/article_confirm_delete.html', {'article': article})


### CRUD for Comment ###
def comment_list(request):
    comments = Comment.objects.select_related('article').all().order_by('-created_at')
    return render(request, 'news/comments.html', {'comments': comments})


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(reverse('news:comment_list'))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'news/comment_form.html', {'form': form, 'action': 'Edit'})


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect(reverse('news:comment_list'))
    return render(request, 'news/comment_confirm_delete.html', {'comment': comment})


### Contact management (read & delete) ###
def contact_list(request):
    contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'news/contacts.html', {'contacts': contacts})


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'news/contact_detail.html', {'contact': contact})


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(reverse('news:contact_list'))
    return render(request, 'news/contact_confirm_delete.html', {'contact': contact})
