class Mp3Player:
    def play(self, filename):
        print(f"Playing MP3 file: {filename}")


class YouTubePlayer:
    def stream_video(self, url):
        print(f"Streaming from YouTube: {url}")


class YouTubeAdapter:
    def __init__(self,youtube_player):
        self.youtube_player=youtube_player

    def youtube_to_mp3(self):
        pass