# models.py
from django.db import models

class YouTubeVideo(models.Model):
    no = models.AutoField(primary_key=True)  # 자동 증가하는 PK
    recommended_music = models.CharField(max_length=256, verbose_name="추천된 노래 제목")
    video_title = models.CharField(max_length=256, verbose_name="동영상 제목")
    video_url = models.URLField(max_length=256, verbose_name="동영상 URL")

    class Meta:
        db_table = 'youtube_video'  # 데이터베이스 테이블 이름
        verbose_name = "유튜브 동영상"
        verbose_name_plural = "유튜브 동영상 목록"

class YouTubePlaylist(models.Model):
    no = models.AutoField(primary_key=True)
    recommended_music = models.CharField(max_length=256, verbose_name="추천된 노래 제목")
    playlist_title = models.CharField(max_length=256, verbose_name="플레이리스트 제목")
    playlist_url = models.URLField(max_length=256, verbose_name="플레이리스트 URL")

    class Meta:
        db_table = 'youtube_playlist'
        verbose_name = "유튜브 플레이리스트"
        verbose_name_plural = "유튜브 플레이리스트 목록"

class SpotifyPlaylist(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, verbose_name="플레이리스트 제목")
    link = models.URLField(max_length=256, verbose_name="플레이리스트 주소")
    cover_image = models.URLField(max_length=256, verbose_name="커버 이미지 링크")

    class Meta:
        db_table = 'spotify_playlist'
        verbose_name = "스포티파이 플레이리스트"
        verbose_name_plural = "스포티파이 플레이리스트 목록"

class NewSong(models.Model):
    title = models.CharField(max_length=256)
    artist = models.CharField(max_length=256)
    video_url = models.URLField(max_length=256)
    platform = models.CharField(max_length=50)
    release_date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.artist}"
    
    class Meta:
        db_table = 'new_songs'
        verbose_name = "신곡"
        verbose_name_plural = "신곡 목록"

class SeasonalPlaylist(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    playlist_url = models.URLField(max_length=256)
    cover_image = models.URLField(max_length=256, blank=True)
    platform = models.CharField(max_length=50)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'seasonal_playlists'
        verbose_name = "시즌별 플레이리스트"
        verbose_name_plural = "시즌별 플레이리스트 목록"

