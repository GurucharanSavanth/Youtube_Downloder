import pytube
import PySimpleGUI as sg
from concurrent.futures import ThreadPoolExecutor

def download_youtube_video(video_url):
    try:
        # Create a YouTube object from the video URL
        yt = pytube.YouTube(video_url)
        
        # Create a thread pool executor with 2 workers
        executor = ThreadPoolExecutor(max_workers=4)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the default download path to the `download` directory
        download_path = "download"

        # Download the video
        video_stream.download(download_path)

        # Print a success message
        sg.popup("Video downloaded successfully!")
        print("Video downloaded successfully!")

    except Exception as e:
        # Print an error message
        print(e)

def download_youtube_playlist(playlist_url):
    try:
        # Create a YouTube playlist object from the playlist URL
        playlist = pytube.Playlist(playlist_url)

        # Create a thread pool executor with 2 workers
        executor = ThreadPoolExecutor(max_workers=5)

        # Download all videos in the playlist in parallel
        futures = []
        for video in playlist.videos:
            future = executor.submit(download_youtube_video, video.url)
            futures.append(future)

        # Wait for all downloads to finish
        for future in futures:
            future.result()

        # Print a success message
        sg.popup("Playlist downloaded successfully!")
    except Exception as e:
        # Print an error message
        print(e)



def main():
    # Create a PySimpleGUI window
    layout = [
        [sg.Text("YouTube Video Downloader")],
        [sg.InputText(key="video_url")],
        [sg.Button("Download Video"), sg.Button("Download Playlist")],
        [sg.Button("Exit")]

    ]
    window = sg.Window("YouTube Video Downloader", layout)

    # Start the main loop
    while True:
        # Get the user input
        event, values = window.read()

        # Check the user input
        if event == "Exit":
            break
        elif event in ("Download Video", "Download Playlist"):
            # Pop-up a message saying don't close the window or terminal while download is in progress
            sg.popup("Don't close the window or terminal while download is in progress! \nHold on tight best quality video are downloded for you ")
            # Download the video or playlist
            if event == "Download Video":
                video_url = values["video_url"]
                download_youtube_video(video_url)
            elif event == "Download Playlist":
                playlist_url = values["video_url"]
                download_youtube_playlist(playlist_url)

    window.close()

if __name__ == "__main__":
    main()
