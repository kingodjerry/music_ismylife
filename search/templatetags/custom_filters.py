# custom_filters.py
from django import template

register = template.Library()

# split 필터: 문자열을 주어진 key로 나누는 필터
@register.filter(name='split')
def split(value, key):
    """Splits the string by the given key."""
    return value.split(key)
