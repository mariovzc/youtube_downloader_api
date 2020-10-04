import logging
import os

from pytube import YouTube


sh = logging.StreamHandler()
logging.basicConfig(format='%(asctime)s |%(name)s|%(levelname)s|%(message)s',
                    level=logging.INFO,
                    handlers=[sh])


class FileHandler:
    def __init__(self, youtube_url):
        
        self.youtube_url = youtube_url
        self.youtube = YouTube(youtube_url)

    def down_load_file(self):
        logging.info(f"Start download for {self.youtube.title}")
        ys = self.youtube.streams.get_highest_resolution()
        file = ys.download(os.path.basename("/tmp"))
        logging.info(f"Download finished for {self.youtube.title}")
        return file


  