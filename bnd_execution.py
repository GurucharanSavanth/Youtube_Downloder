import pytube
import os
import PySimpleGUI as sg

def download_video(video_url, folder_path=None):
    if folder_path is None:
        folder_path = os.path.join(os.path.expanduser("~"), "Downloads")

    video = pytube.YouTube(video_url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=os.path.join(folder_path, video.title + ".mp4"))

def main():
    layout = [
        [sg.Text("Enter YouTube video URL:")],
        [sg.InputText("", key="video_url")],
        [sg.FolderBrowse(key="folder_path")],
        [sg.Button("Download")],
    ]
    window = sg.Window("YouTube Video Downloader", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Download":
            if not values["video_url"]:
                sg.popup("Please enter a YouTube video URL.")
                continue
            download_video(values["video_url"], values["folder_path"])
            sg.popup("Video downloaded successfully!")

    window.close()

if __name__ == "__main__":
    main()

