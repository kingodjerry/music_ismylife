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
});

document.addEventListener('DOMContentLoaded', () => {
    // 플로팅 버튼과 모달
    const openModalBtn = document.getElementById('open-modal-btn');
    const closeModalBtn = document.getElementById('close-modal-btn');
    const modal = document.getElementById('modal');

    // 모달 열기
    openModalBtn.addEventListener('click', () => {
        modal.style.display = 'block'; // 모달을 보이도록 설정
    });

    // 모달 닫기
    closeModalBtn.addEventListener('click', () => {
        modal.style.display = 'none'; // 모달을 숨김
    });

    // 모달 외부 클릭 시 닫기
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            modal.style.display = 'none'; // 모달을 숨김
        }
    });
});