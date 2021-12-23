from rest_framework import serializers

from django.contrib.auth.models import User
from ytsearch.models import SearchResults

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SearchResults
        fields = ('video_id', 'title', 'description', 'search_query', 'publish_datetime', 'thumbnail_url')
