

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    image = models.ImageField(upload_to='news/')
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    def __str__(self):
        subject = (self.subject[:30] + '...') if self.subject and len(self.subject) > 30 else (self.subject or '')
        return f"{self.name} <{self.email}> - {subject}"


class Comment(models.Model):
    article = models.ForeignKey(
        NewsArticle,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} on {self.article.title}"
