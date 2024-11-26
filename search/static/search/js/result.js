document.addEventListener('DOMContentLoaded', () => {
    const youtubeButton = document.getElementById('youtube-button');
    const spotifyButton = document.getElementById('spotify-button');
    const youtubeSection = document.getElementById('youtube-section');
    const spotifySection = document.getElementById('spotify-section');

    // YouTube 버튼 클릭
    youtubeButton.addEventListener('click', () => {
        youtubeSection.classList.remove('hidden');
        spotifySection.classList.add('hidden');
        youtubeButton.classList.add('active');
        spotifyButton.classList.remove('active');
    });

    // Spotify 버튼 클릭
    spotifyButton.addEventListener('click', () => {
        spotifySection.classList.remove('hidden');
        youtubeSection.classList.add('hidden');
        spotifyButton.classList.add('active');
        youtubeButton.classList.remove('active');
    });

    // 플레이리스트 저장 배열
    let playlist = [];
    let currentVideoIndex = -1;  // 현재 재생 중인 비디오 인덱스

    // 담기 버튼 클릭 시 플레이리스트에 노래 추가
    function addToPlaylist(title, url) {
        if (!playlist.some(video => video.url === url)) {
            playlist.push({ title: title, url: url });
            updatePlaylist(); // 플레이리스트 업데이트
            showToast(`"${title}"가 플레이리스트에 추가되었습니다!`);
        } else {
            console.log("이 노래는 이미 플레이리스트에 있습니다.");
        }
    }

    // 플레이리스트 업데이트 함수
    function updatePlaylist() {
        const videoList = document.getElementById('video-list');
        videoList.innerHTML = ''; // 기존 리스트를 비우고

        playlist.forEach((video, index) => {
            const listItem = document.createElement('li');
            listItem.classList.add('song-item');
            listItem.innerHTML = `<p class="song-title">${video.title}</p>`;
            videoList.appendChild(listItem);
        });
    }

    // 비디오 재생 함수
    function playVideo(index) {
        currentVideoIndex = index;
        const video = playlist[index];
        const youtubePlayer = document.getElementById('youtube-player');
        
        // 비디오 ID 추출
        const videoId = getVideoIdFromUrl(video.url);
        if (videoId) {
            youtubePlayer.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&enablejsapi=1`;
        } else {
            console.log('비디오 ID를 추출할 수 없습니다. URL을 확인하세요.');
        }
        
        // 모달 열기
        const modal = document.getElementById('modal');
        modal.style.display = 'block';
    }

    // YouTube URL에서 비디오 ID 추출
    function getVideoIdFromUrl(url) {
        const videoIdRegex = /(?:https?:\/\/(?:www\.)?youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=))([a-zA-Z0-9_-]{11})/;
        const match = url.match(videoIdRegex);
        return match ? match[1] : null;
    }

    const showToast = (message) => {
        const toast = document.getElementById("toast");
        toast.textContent = message;
        toast.classList.add("show");
        setTimeout(() => toast.classList.remove("show"), 3000);
    };

    // "담기" 버튼 클릭 시, 제목과 URL을 가져와 addToPlaylist 호출
    const addButtons = document.querySelectorAll('.view-btn');
    addButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault(); // 페이지 이동 방지
            const url = button.getAttribute('href'); // 비디오의 URL
            const title = button.getAttribute('data-title'); // 'data-title' 속성으로 제목 가져오기
            addToPlaylist(title, url); // 플레이리스트에 추가
        });
    });

    // 모달 열기 버튼 설정
    const modal = document.getElementById("modal");
    const openModalBtn = document.getElementById("open-modal-btn");
    const closeModalBtn = document.getElementById("close-modal-btn");

    openModalBtn.addEventListener('click', () => {
        if (playlist.length === 0) {
            showToast("플레이리스트가 비어 있습니다!");
            return;
        }
        
        if (currentVideoIndex === -1 && playlist.length > 0) {
            playVideo(0);  // 첫 번째 비디오 재생 시작
        } else {
            modal.style.display = 'block';
            playCurrentTrack();
        }
        
        document.body.style.overflow = 'hidden';  // 모달 열릴 때 스크롤 방지
    });

    closeModalBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = '';  // 모달 닫을 때 스크롤 복원
        youtubePlayer.src = '';  // 모달 닫을 때 비디오 초기화
    });

    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModalBtn.click();  // 외부 클릭 시 모달 닫기 트리거
        }
    });

    // 이전, 재생, 일시정지, 다음 버튼 동작 설정
    document.getElementById('prev-btn').addEventListener('click', () => {
        if (currentVideoIndex > 0) {
            playVideo(currentVideoIndex - 1);
        }
    });

    document.getElementById('next-btn').addEventListener('click', () => {
        if (currentVideoIndex < playlist.length - 1) {
            playVideo(currentVideoIndex + 1);
        }
    });
});