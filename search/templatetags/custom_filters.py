# custom_filters.py
from django import template
from ..models import DailySongs  # models를 임포트

register = template.Library()

# split 필터: 문자열을 주어진 key로 나누는 필터
@register.filter(name='split')
def split(value, key):
    """Splits the string by the given key."""
    return value.split(key)

register = template.Library()

# youtube_url 필터: YouTube URL을 완성하는 필터
@register.filter
def youtube_url(song):
    """
    YouTube URL을 완성하는 필터.
    플랫폼이 유튜브이고 URL이 완성되지 않았으면 YouTube 기본 URL을 붙임.
    """
    if isinstance(song, DailySongs):  # song이 DailySongs 인스턴스인지 확인
        if song.platform == "youtube" and not song.song_url.startswith("http"):
            return f"https://www.youtube.com/watch?v={song.song_url}"
        return song.song_url
    return ""  # song이 올바른 인스턴스가 아닐 경우 빈 문자열 반환

