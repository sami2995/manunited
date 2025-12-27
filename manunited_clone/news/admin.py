from django.contrib import admin
from .models import Category, NewsArticle
from .models import Category, NewsArticle, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'published_at')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'created_at', 'handled')
	list_filter = ('handled', 'created_at')
