from django.db import models
import datetime
from django.db.models.deletion import CASCADE, SET_NULL

from django.utils import text

class User(models.Model):
    user = models.ForeignKey(to='auth.User', on_delete=models.cascade)
    profile_photo = models.ImageField()
    bio = models.TextField()

class Article(models.Model):
    author = models.ForeignKey(to=User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(to='articles.Category', related_name='articles', on_delete=models.SET_NULL)
    tags = models.ArrayField(base_field=models.CharField(max_length=255))

class Comment(models.Model):
    article = models.ForeignKey(to=Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='comments', on_delete=models.CASCADE)
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
