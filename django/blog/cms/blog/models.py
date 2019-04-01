from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    STATUS_CHOIES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=160)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE,)
    published = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOIES, default='draft')
        
    def __str__(self):
        return self.title