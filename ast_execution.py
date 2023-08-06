import pytube
import PySimpleGUI as sg
import os
import threading

def download_playlist(playlist_url, download_path):
  playlist = pytube.Playlist(playlist_url)
  download_thread = threading.Thread(target=_download_playlist, args=(playlist, download_path))
  download_thread.daemon = True
  download_thread.start()

def _download_playlist(playlist, download_path):
  i = 0
  downloaded_files = 0
  while i < len(playlist.videos):
    stream = playlist.videos[i].streams.get_highest_resolution()
    stream.download(download_path)
    i += 1
    downloaded_files += 1

  def show_progress():
    while downloaded_files < len(playlist.videos):
      popup = sg.popup(f"{downloaded_files} files downloaded, {len(playlist.videos) - downloaded_files} files left.")
      popup.update(f"{downloaded_files} files downloaded, {len(playlist.videos) - downloaded_files} files left.")
      downloaded_files += 1

  main_thread = threading.Thread(target=show_progress)
  main_thread.start()

def handle_exception(exception):
  if exception == "Empty Download Text Area":
    popup = sg.popup("Please enter a YouTube playlist URL.")
  elif exception == "Empty Download Path":
    popup = sg.popup("Please enter a download path.")
  else:
    popup = sg.popup(exception)

if __name__ == "__main__":
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
      if not playlist_url:
        handle_exception("Empty Download Text Area")
      elif not download_path:
        handle_exception("Empty Download Path")
      else:
        download_playlist(playlist_url, download_path)
