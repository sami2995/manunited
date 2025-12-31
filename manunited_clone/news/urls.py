from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    # Articles
    path('articles/', views.article_list, name='article_list'),
    path('articles/add/', views.article_add, name='article_add'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
    # Comments
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    # Contacts
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]
