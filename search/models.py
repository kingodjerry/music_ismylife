# models.py
from django.db import models

# 플랫폼 선택지 ENUM 정의
class PlatformEnum(models.TextChoices):
    YOUTUBE = 'youtube', 'YouTube'
    SPOTIFY = 'spotify', 'Spotify'


# DailySongs 모델
class DailySongs(models.Model):
    no = models.AutoField(primary_key=True)
    song_title = models.CharField(max_length=255, verbose_name="Song Title")
    song_url = models.URLField(max_length=255, verbose_name="Song URL")
    thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    platform = models.CharField(
        max_length=10,
        choices=PlatformEnum.choices,
        verbose_name="Platform",
    )

    class Meta:
        db_table = 'daily_songs'
        verbose_name = 'Daily Song'
        verbose_name_plural = 'Daily Songs'


# DailyPlaylists 모델
class DailyPlaylists(models.Model):
    no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    playlist_title = models.CharField(max_length=252, verbose_name="Playlist Title")
    playlist_url = models.URLField(max_length=255, verbose_name="Playlist URL")
    thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    platform = models.CharField(
        max_length=10,
        choices=PlatformEnum.choices,
        verbose_name="Platform",
    )

    class Meta:
        db_table = 'daily_playlists'
        verbose_name = 'Daily Playlist'
        verbose_name_plural = 'Daily Playlists'


# SearchSongs 모델
class SearchSongs(models.Model):
    no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    song_title = models.CharField(max_length=255, verbose_name="Song Title")
    song_url = models.URLField(max_length=255, verbose_name="Song URL")
    thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    platform = models.CharField(
        max_length=10,
        choices=PlatformEnum.choices,
        verbose_name="Platform",
    )

    class Meta:
        db_table = 'search_songs'
        verbose_name = 'Search Song'
        verbose_name_plural = 'Search Songs'


# SearchPlaylist 모델
class SearchPlaylist(models.Model):
    no = models.AutoField(primary_key=True)  # 기본 키를 'no'로 설정
    playlist_title = models.CharField(max_length=252, verbose_name="Playlist Title")
    playlist_url = models.URLField(max_length=255, verbose_name="Playlist URL")
    thumbnail = models.URLField(max_length=255, null=True, blank=True, verbose_name="Thumbnail")
    platform = models.CharField(
        max_length=10,
        choices=PlatformEnum.choices,
        verbose_name="Platform",
    )

    class Meta:
        db_table = 'search_playlist'
        verbose_name = 'Search Playlist'
        verbose_name_plural = 'Search Playlists'
