from django.db import models

class SearchResults(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    search_query = models.CharField(max_length=255)
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()
    duration = models.DurationField()
    video_id = models.CharField(max_length=10)

    def __str__(self):
        return self.video_id