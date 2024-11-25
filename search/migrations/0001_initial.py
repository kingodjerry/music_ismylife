# Generated by Django 5.1.3 on 2024-11-24 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('artist', models.CharField(max_length=256)),
                ('video_url', models.URLField(max_length=256)),
                ('platform', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
            ],
            options={
                'verbose_name': '신곡',
                'verbose_name_plural': '신곡 목록',
                'db_table': 'new_songs',
            },
        ),
        migrations.CreateModel(
            name='SeasonalPlaylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('playlist_url', models.URLField(max_length=256)),
                ('cover_image', models.URLField(blank=True, max_length=256)),
                ('platform', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '시즌별 플레이리스트',
                'verbose_name_plural': '시즌별 플레이리스트 목록',
                'db_table': 'seasonal_playlists',
            },
        ),
        migrations.CreateModel(
            name='SpotifyPlaylist',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='플레이리스트 제목')),
                ('link', models.URLField(max_length=256, verbose_name='플레이리스트 주소')),
                ('cover_image', models.URLField(max_length=256, verbose_name='커버 이미지 링크')),
            ],
            options={
                'verbose_name': '스포티파이 플레이리스트',
                'verbose_name_plural': '스포티파이 플레이리스트 목록',
                'db_table': 'spotify_playlist',
            },
        ),
        migrations.CreateModel(
            name='YouTubePlaylist',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('recommended_music', models.CharField(max_length=256, verbose_name='추천된 노래 제목')),
                ('playlist_title', models.CharField(max_length=256, verbose_name='플레이리스트 제목')),
                ('playlist_url', models.URLField(max_length=256, verbose_name='플레이리스트 URL')),
            ],
            options={
                'verbose_name': '유튜브 플레이리스트',
                'verbose_name_plural': '유튜브 플레이리스트 목록',
                'db_table': 'youtube_playlist',
            },
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('recommended_music', models.CharField(max_length=256, verbose_name='추천된 노래 제목')),
                ('video_title', models.CharField(max_length=256, verbose_name='동영상 제목')),
                ('video_url', models.URLField(max_length=256, verbose_name='동영상 URL')),
            ],
            options={
                'verbose_name': '유튜브 동영상',
                'verbose_name_plural': '유튜브 동영상 목록',
                'db_table': 'youtube_video',
            },
        ),
    ]