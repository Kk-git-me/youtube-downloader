from pytube import YouTube
import time

class youtube_video:
    def __init__(self):
        pass

    def set_link(self,link):
        self.link = link

    def get_streams(self):
        self.streams = self.__link.streams.filter(
            progressive=True,
            file_extension='mp4'
        )

    def get_video_sizes(self):
        sizes = map(lambda x : f"{x.filesize_mb} MB",self.streams)
        return list(sizes)

    def get_video_info(self):
        sizes = self.get_video_sizes()
        return f"""
        Title: {self.__link.title},
        Length: {time.strftime('%H:%M:%S',time.gmtime(self.__link.length))},
        Size-720p: {sizes[1]},
        Size-360p: {sizes[0]},
        """
    def download_360p(self,path='/home/kk/Videos',ind='1.'):
        self.streams.first().download(path,filename_prefix=ind)

    def download_720p(self,path='/home/kk/Videos',ind='1.'):
        self.streams.last().download(path,filename_prefix=ind)


def get_youtube_object(link):
    return YouTube(link)

if __name__ == "__main__":
    link = input("Enter Link: ")
    yv = youtube_video(link)
    yv.get_streams()
    print(yv.get_video_info())
    yv.download_360p()
