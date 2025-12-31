from django import forms
from .models import Contact, Category, NewsArticle, Comment


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': "What's on your mind?",
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Category Name'}),
        }


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = ['title', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'comment']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
