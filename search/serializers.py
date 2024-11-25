from rest_framework import serializers
from .models import YouTubeVideo, YouTubePlaylist, SpotifyPlaylist

class YouTubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubeVideo
        fields = ['id', 'recommended_music', 'video_title', 'video_url']

class YouTubePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTubePlaylist
        fields = ['id', 'recommended_music', 'playlist_title', 'playlist_url']

class SpotifyPlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpotifyPlaylist
        fields = ['id', 'title', 'link', 'cover_image']
