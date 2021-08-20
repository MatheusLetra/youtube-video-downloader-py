import PySimpleGUI
from youtube_dowloader import  YoutubeDownloader


class Screen:
    def __init__(self):
        self.inputs_column = [
            [
                PySimpleGUI.Text("Pasta para Download",size=(20, 1)),
                PySimpleGUI.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                PySimpleGUI.FolderBrowse('Escolher'),
            ],
            [
                PySimpleGUI.Text("Link do Video",size=(20, 1)),
                PySimpleGUI.In(size=(25, 1), enable_events=True, key="-VIDEO_LINK-"),
                PySimpleGUI.Checkbox(
                    'Somente Áudio', key='-ONLY_AUDIO-', enable_events=True)
            ]
        ]
        self.layout = [
                        [PySimpleGUI.Text("Bem-vindo ao Youtube Video Downloader")],
                        [
                            PySimpleGUI.Column(self.inputs_column),
                        ],
                        [PySimpleGUI.Button(button_text="Download", enable_events=True, key="-DOWNLOAD_VIDEO-")],
                        [],
                        [PySimpleGUI.Text("Desenvolvido por Matheus Letra")],
                    ]

        self.window = PySimpleGUI.Window(title='Youtube Video Downloader', layout= self.layout)


    def Show(self):
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
                break

            if event == "-DOWNLOAD_VIDEO-":
                folder = values["-FOLDER-"]
                url = values["-VIDEO_LINK-"]

                if (folder != '' and url != ''):
                    try:
                        yt = YoutubeDownloader(url, folder)
                        yt.Download(values["-ONLY_AUDIO-"])
                    except:
                        PySimpleGUI.PopupError('Erro ao baixar vídeo...', no_titlebar=True)
                else:
                    PySimpleGUI.Popup('Informe a Pasta e o Link do Vídeo!', no_titlebar=True)





