

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
