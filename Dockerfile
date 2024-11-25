# 1. Python 3.9 슬림 이미지를 기반으로 설정
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app/music_ismylife

# 3. 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Django 애플리케이션 소스 코드 복사 (secrets.json 포함)
COPY . .

# 5. Django의 기본 포트 8000을 노출
EXPOSE 8000

# 6. Django 서버 실행 (0.0.0.0으로 모든 외부 IP에서 접근 가능하도록)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]