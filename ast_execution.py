import pytube
import PySimpleGUI as sg
import os

def download_playlist(playlist_url, download_path):
  playlist = pytube.Playlist(playlist_url)
  i = 0
  while i < len(playlist.videos):
    stream = playlist.videos[i].streams.get_highest_resolution()
    stream.download(download_path)
    i += 1

def main():
  layout = [
    [sg.Text("Enter the YouTube playlist URL:")],
    [sg.InputText(), sg.Button("Download")],
    [sg.Text("Download Path:"), sg.InputText(), sg.FolderBrowse()],
  ]
  window = sg.Window("YouTube Playlist Downloader", layout)
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "Download":
      playlist_url = values[0]
      download_path = values[1]
      download_playlist(playlist_url, download_path)

if __name__ == "__main__":
  main()
