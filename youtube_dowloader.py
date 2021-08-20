import pytube
import PySimpleGUI

class YoutubeDownloader:
    def __init__(self, Url,Path):
        self.__VideoUrl = Url
        self.__YoutubeVideo = pytube.YouTube(self.__VideoUrl)
        self.__VideoStream = self.__YoutubeVideo.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        self.__outputPath = Path

    def Download(self, OnlyAudio):
        if (OnlyAudio):
            self.__VideoStream = self.__YoutubeVideo.streams.filter(only_audio=True).first()
            self.__VideoStream.download(output_path=self.__outputPath, filename=self.__YoutubeVideo.title + '.mp3')
            PySimpleGUI.Popup('Aúdio: "{}" baixado com Sucesso!'.format(self.__YoutubeVideo.title), no_titlebar=True)
        else:
            self.__VideoStream.download(output_path=self.__outputPath)
            PySimpleGUI.Popup('Vídeo: "{}" baixado com Sucesso!'.format(self.__YoutubeVideo.title), no_titlebar=True)