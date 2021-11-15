from django.db import models
import datetime
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.postgres.fields import ArrayField
from ckeditor_uploader.fields import RichTextUploadingField

class User(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=CASCADE)
    profile_photo = models.ImageField()
    bio = models.TextField()

class Article(models.Model):
    author = models.ForeignKey(to=User, related_name='articles', on_delete=CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    slug = models.SlugField()
    description = models.TextField()
    text = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to='articles.Category', related_name='articles', on_delete=SET_NULL, null=True)
    # tags = ArrayField(base_field=models.CharField(max_length=255))
    time_to_read = models.IntegerField(default=10)
    views_count = models.IntegerField(default=0)

class Comment(models.Model):
    article = models.ForeignKey(to=Article, related_name='comments', on_delete=CASCADE)
    user = models.ForeignKey(to=User, related_name='comments', on_delete=CASCADE)
    slug = models.SlugField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
