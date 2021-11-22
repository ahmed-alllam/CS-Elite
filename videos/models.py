from django.db import models

class YoutubeVideo(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField()
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField()
    duration = models.CharField(max_length=10)

    class Meta:
        ordering = ('-created_at',)
