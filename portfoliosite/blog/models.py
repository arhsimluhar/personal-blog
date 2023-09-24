from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices,
                              default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')

    objects = models.Manager()
    published_manager = PublishedManager()

    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'], name='published_idx'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])
