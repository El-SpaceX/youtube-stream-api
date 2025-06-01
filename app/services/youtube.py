import yt_dlp, requests
from youtubesearchpython import VideosSearch

class AudioUrl:
    yt_audio_url: str
    def __init__(self, audio_url: str):
        self.yt_audio_url = audio_url

    def isValid(self) -> bool:
        return len(self.yt_audio_url)

    def generate_audio(self):
        with requests.get(self.yt_audio_url, stream=True) as r:
            r.raise_for_status()
            for chunk in r.iter_content(chunk_size=1024):
                yield chunk


class YoutubeStream:
    def __init__(self):
        pass

    def get_audio_url(self, youtube_url: str) -> AudioUrl:
        try:
            ydl_opts = {
                'format': 'bestaudio/best',  
                'quiet': True,              
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=False)
                audio_url = info['url']

            return AudioUrl(audio_url)

        except Exception as e:
            return AudioUrl("")


    def searchVideo(self, query: str, max_results=5):
        videos_search = VideosSearch(query, limit=max_results)
        result = videos_search.result()

        videos = []
        for video in result["result"]:
            video_data = {
                "title": video["title"],
                "url": f"https://www.youtube.com/watch?v={video['id']}",
                "duration" : video["duration"] 
            }
            videos.append(video_data)
        
        return videos