from django.db import models

class SearchResults(models.Model):
    video_id = models.CharField(max_length=16, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    search_query = models.CharField(max_length=120)
    publish_datetime = models.DateTimeField()
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.video_id