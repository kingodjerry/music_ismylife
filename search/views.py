from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import YouTubeVideo, YouTubePlaylist, SpotifyPlaylist, NewSong, SeasonalPlaylist
from .serializers import (
    YouTubeVideoSerializer, 
    YouTubePlaylistSerializer, 
    SpotifyPlaylistSerializer
)

def index(request):
    new_songs = NewSong.objects.all()[:10]  # 최신 10개
    playlists = SeasonalPlaylist.objects.all()[:10]  # 10개
    
    print(f"New songs: {new_songs}")  # 디버깅용 출력
    print(f"Playlists: {playlists}")  # 디버깅용 출력
    
    context = {
        'new_songs': new_songs,
        'playlists': playlists,
    }
    return render(request, 'search/index.html', context)

import requests
from requests.auth import HTTPBasicAuth

@csrf_exempt  # CSRF 방지 비활성화 (외부 요청에만 사용)
def trigger_airflow_dag(request):
    if request.method == "POST":
        # 폼 데이터에서 입력값과 플랫폼 가져오기
        input_value = request.POST.get("input_value")
        platform = request.POST.get("platform")  # 'youtube' 또는 'spotify'

        # 입력값이 없으면 에러 반환
        if not input_value:
            return JsonResponse({"error": "검색어를 입력해주세요!"}, status=400)
        
        # 플랫폼 선택이 없으면 에러 반환
        if not platform:
            return JsonResponse({"error": "검색 플랫폼을 선택해주세요!"}, status=400)

        airflow_url = "http://localhost:8080/api/v1/dags/example_trigger_dag/dagRuns"
        username = 'airflow'
        password = 'airflow'

        # payload 설정
        payload = {
            "conf": {"input_value": input_value, "platform": platform}
        }

        headers = {
            'Content-Type': 'application/json',  # 요청 본문 형식
            'Accept': 'application/json',        # 응답 형식
        }

        try:
            # Airflow API에 요청
            response = requests.post(airflow_url, json=payload, headers=headers, auth=HTTPBasicAuth(username, password))

            if response.status_code == 200:
                return JsonResponse({"message": "DAG triggered successfully!"})
            else:
                return JsonResponse({"error": response.json()}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)


def result(request):    
    # 모든 데이터 가져오기
    youtube_videos = YouTubeVideo.objects.all()
    youtube_playlists = YouTubePlaylist.objects.all()
    spotify_playlists = SpotifyPlaylist.objects.all()

    # 템플릿으로 데이터 전달
    context = {
        'youtube_videos': youtube_videos,
        'youtube_playlists': youtube_playlists,
        'spotify_playlists': spotify_playlists,
    }
    return render(request, 'search/result.html', context)

