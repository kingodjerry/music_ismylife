# Spotify와 Youtube API 기반 음악 추천 웹앱 🎵
해당 프로젝트는 Spotify, Youtube API를 활용한 **검색어 기반 노래 추천 서비스**입니다. 이 프로젝트는 Docker 환경에서 실행되도록 구현했고, Airflow 기반 ETL 자동화, Django 기반 웹앱 구현을 목표로 했습니다. 파이프라인을 통해 원활한 ELT(Extract, Load, Transform) 프로세스가 진행되며, 해당 DAG는 Airflow REST API를 사용하여 웹앱에서 검색어를 입력받아 트리거하도록 구현했습니다. 사용자가 검색어를 입력하면 Spotify와 Youtube API를 호출하는 DAG가 트리거되어, API의 음악 추천 알고리즘을 직접적으로 사용하는 방식을 채택하였습니다. 

<img width="639" alt="home_page" src="https://github.com/user-attachments/assets/61daa05b-5dac-49a4-b4e4-783b875bca2f">
<img width="637" alt="result_page" src="https://github.com/user-attachments/assets/e0a34d03-dd20-4b7d-8296-3a1eed5cd5b1">
<img width="637" alt="result_page2" src="https://github.com/user-attachments/assets/6a6698b5-b59b-4c28-8bdc-428a93da3309">

