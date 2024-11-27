-- SQLBook: Code
-- daily_songs 테이블에 더미 데이터 삽입
INSERT INTO django_schema.daily_songs (song_title, song_url, thumbnail, platform)
VALUES 
('Blinding Lights', 'https://www.youtube.com/watch?v=fHI8X4OXluQ', 'https://img.youtube.com/vi/fHI8X4OXluQ/hqdefault.jpg', 'youtube'),
('Shape of You', 'https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3', 'https://i.scdn.co/image/ab67616d0000b273f3c3f3f3f3f3f3f3f3f3f3f3', 'spotify'),
('Levitating', 'https://www.youtube.com/watch?v=TUVcZfQe-Kw', 'https://img.youtube.com/vi/TUVcZfQe-Kw/hqdefault.jpg', 'youtube'),
('Peaches', 'https://open.spotify.com/track/4iJyoBOLtHqaGxP12qzhQI', 'https://i.scdn.co/image/ab67616d0000b273d6d9d6d9d6d9d6d9d6d9d6d9', 'spotify'),
('Save Your Tears', 'https://www.youtube.com/watch?v=XXYlFuWEuKI', 'https://img.youtube.com/vi/XXYlFuWEuKI/hqdefault.jpg', 'youtube'),
('Good 4 U', 'https://open.spotify.com/track/6PERP62TejQjgHu81OHxgM', 'https://i.scdn.co/image/ab67616d0000b273a5a5a5a5a5a5a5a5a5a5a5a5', 'spotify'),
('Stay', 'https://www.youtube.com/watch?v=kTJczUoc26U', 'https://img.youtube.com/vi/kTJczUoc26U/hqdefault.jpg', 'youtube'),
('drivers license', 'https://open.spotify.com/track/5wANPM4fQCJwkGd4rN57mH', 'https://i.scdn.co/image/ab67616d0000b273b7b7b7b7b7b7b7b7b7b7b7b7', 'spotify'),
('Montero (Call Me By Your Name)', 'https://www.youtube.com/watch?v=6swmTBVI83k', 'https://img.youtube.com/vi/6swmTBVI83k/hqdefault.jpg', 'youtube'),
('Kiss Me More', 'https://open.spotify.com/track/748mdHapucXQri7IAO8yFK', 'https://i.scdn.co/image/ab67616d0000b273c8c8c8c8c8c8c8c8c8c8c8c8', 'spotify');

-- daily_playlists 테이블에 더미 데이터 삽입
INSERT INTO django_schema.daily_playlists (playlist_title, playlist_url, thumbnail, platform)
VALUES 
('Top Hits 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/playlist1/hqdefault.jpg', 'youtube'),
('Chill Vibes 2024', 'https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6', 'https://i.scdn.co/image/ab67706f00000003e8e28219724c2423afa4d320', 'spotify'),
('Workout Mix 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0iYL6RCwyVLxLZG9P8Rr4x0B', 'https://img.youtube.com/vi/playlist2/hqdefault.jpg', 'youtube'),
('Party Hits 2024', 'https://open.spotify.com/playlist/37i9dQZF1DXa2PvUpywmrr', 'https://i.scdn.co/image/ab67706f00000003c0c633b7590b647e2bafaf23', 'spotify'),
('Relax & Unwind 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/playlist3/hqdefault.jpg', 'youtube'),
('Focus Music 2024', 'https://open.spotify.com/playlist/37i9dQZF1DX8NTLI2TtZa6', 'https://i.scdn.co/image/ab67706f000000034ca5a7aed5c4b2aa48136043', 'spotify'),
('Pop Classics 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/playlist4/hqdefault.jpg', 'youtube'),
('Indie Essentials 2024', 'https://open.spotify.com/playlist/37i9dQZF1DX2Nc3B70tvx0', 'https://i.scdn.co/image/ab67706f000000038ed1a5002b96c2ea882541b2', 'spotify'),
('Rock Anthems 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/playlist5/hqdefault.jpg', 'youtube'),
('Jazz Classics 2024', 'https://open.spotify.com/playlist/37i9dQZF1DXbITWG1ZJKYt', 'https://i.scdn.co/image/ab67706f00000003a0e7a1e94f31f7613a4523c9', 'spotify');

-- search_songs 테이블에 더미 데이터 삽입
INSERT INTO django_schema.search_songs (song_title, song_url, thumbnail, platform)
VALUES 
('Bad Habits', 'https://www.youtube.com/watch?v=orJSJGHjBLI', 'https://img.youtube.com/vi/orJSJGHjBLI/hqdefault.jpg', 'youtube'),
('Industry Baby', 'https://open.spotify.com/track/5Z9KJZvQzH6PFmb8SNkxuk', 'https://i.scdn.co/image/ab67616d0000b273ba26678947112dff3c3158bf', 'spotify'),
('Butter', 'https://www.youtube.com/watch?v=WMweEpGlu_U', 'https://img.youtube.com/vi/WMweEpGlu_U/hqdefault.jpg', 'youtube'),
('Deja Vu', 'https://open.spotify.com/track/6HU7h9RYOaPRFeh0R3UeAr', 'https://i.scdn.co/image/ab67616d0000b273a91c10fe9472d9bd89802e5a', 'spotify'),
('Permission to Dance', 'https://www.youtube.com/watch?v=CuklIb9d3fI', 'https://img.youtube.com/vi/CuklIb9d3fI/hqdefault.jpg', 'youtube'),
('Take My Breath', 'https://open.spotify.com/track/6OGogr19zPTM4BALXuMQpF', 'https://i.scdn.co/image/ab67616d0000b273f7f74100d5cc850e01e26c9a', 'spotify'),
('Leave the Door Open', 'https://www.youtube.com/watch?v=adLGHcj_fmA', 'https://img.youtube.com/vi/adLGHcj_fmA/hqdefault.jpg', 'youtube'),
('Heartbreak Anthem', 'https://open.spotify.com/track/5K6Ssv4Z3zRvxt0P6EKUAP', 'https://i.scdn.co/image/ab67616d0000b2736ef7f6d1e0fcf25307a6f37c', 'spotify'),
('Peaches (feat. Daniel Caesar & Giveon)', 'https://www.youtube.com/watch?v=tQ0yjYUFKAE', 'https://img.youtube.com/vi/tQ0yjYUFKAE/hqdefault.jpg', 'youtube'),
('Save Your Tears (with Ariana Grande)', 'https://open.spotify.com/track/37BZB0z9T8Xu7U3e65qxFy', 'https://i.scdn.co/image/ab67616d0000b273304b5df68ba4ee6ee2a09fc4', 'spotify');

-- search_playlists 테이블에 더미 데이터 삽입
INSERT INTO django_schema.search_playlist (playlist_title, playlist_url, thumbnail, platform)
VALUES 
('Summer Hits 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/summerhits24/hqdefault.jpg', 'youtube'),
('Acoustic Covers 2024', 'https://open.spotify.com/playlist/37i9dQZF1DWXmlLSKkfdAk', 'https://i.scdn.co/image/ab67706f00000003f6b55ca93bd33211227b6c60', 'spotify'),
('Hip-Hop Bangers 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/hiphopbangers24/hqdefault.jpg', 'youtube'),
('Classical Essentials 2024', 'https://open.spotify.com/playlist/37i9dQZF1DWWEJlAGA9gs0', 'https://i.scdn.co/image/ab67706f000000035ffa3e6c8de2a0c5c4d0ffc5', 'spotify'),
('Feel Good Tunes 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/feelgoodtunes24/hqdefault.jpg', 'youtube'),
('Electronic Beats 2024', 'https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO', 'https://i.scdn.co/image/ab67706f000000034df02702aa0d8e4f46e7d2f0', 'spotify'),
('Latin Vibes 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/latinvibes24/hqdefault.jpg', 'youtube'),
('Soul Classics 2024', 'https://open.spotify.com/playlist/37i9dQZF1DX9XIFQuFvzM4', 'https://i.scdn.co/image/ab67706f0000000324f4d1b5d4f1c5e8e3e2c9a9', 'spotify'),
('Reggae Rhythms 2024', 'https://www.youtube.com/playlist?list=PLHPTxTxtC0ibVZrT2_WKWUl2SAxsKuKwx', 'https://img.youtube.com/vi/reggaerhythms24/hqdefault.jpg', 'youtube'),
('Blues Legends 2024', 'https://open.spotify.com/playlist/37i9dQZF1DXd9rSDyQguIk', 'https://i.scdn.co/image/ab67706f00000003e6e2e0f7c3f3e3e3e3e3e3e3', 'spotify');