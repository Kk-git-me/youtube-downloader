from youtube_video import *
from pytube import Playlist

class youtube_playlist(youtube_video):
    def __init__(self, link):
        self.playlist = Playlist(link)
    
    def youtube_video_links(self):
        self.video_urls = self.playlist.videos

    def playlistInfo(self):
        return(f"""
            Title: {self.playlist.title},
            Total available Videos: {self.playlist.length}
        """)

    