import pytube

def download_youtube_video(video_url):
    try:
        # Create a YouTube object from the video URL
        yt = pytube.YouTube(video_url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the default download path to the `download` directory
        download_path = "download"

        # Download the video
        video_stream.download(download_path)

        # Print a success message
        print("Video downloaded successfully!")
    except Exception as e:
        # Print an error message
        print(e)

if __name__ == "__main__":
    # Get the video URL from the user
    video_url = input("Enter the YouTube video URL: ")

    # Download the video
    download_youtube_video(video_url)
