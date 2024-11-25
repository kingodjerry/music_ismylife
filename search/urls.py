from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('trigger-dag/', views.trigger_airflow_dag, name='trigger_dag'),  # Airflow 트리거 URL
    path('result/', views.result, name='result'),  # 결과 페이지
]
