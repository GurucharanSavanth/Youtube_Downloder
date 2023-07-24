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

def download_youtube_playlist(playlist_url):
    try:
        # Create a YouTube playlist object from the playlist URL
        playlist = pytube.Playlist(playlist_url)

        # Download all videos in the playlist
        for video in playlist.videos:
            video_stream = video.streams.get_highest_resolution()
            video_stream.download(download_path)

        # Print a success message
        print("Playlist downloaded successfully!")
    except Exception as e:
        # Print an error message
        print(e)

def main():
    # Create a queue to store the video links
    queue = []

    # Start the main loop
    while True:
        # Print the menu
        print("1. Enqueue video")
        print("2. Enqueue playlist")
        print("3. Downlode the listed videos if done ")
        print("4. Exit")

        # Get the user input
        choice = input("Enter your choice: ")

        # Check the user input
        if choice == "1":
            # Get the video URL
            video_url = input("Enter the YouTube video URL: ")

            # Enqueue the video
            queue.append(video_url)
        elif choice == "2":
            # Get the playlist URL
            playlist_url = input("Enter the YouTube playlist URL: ")

            # Enqueue the playlist
            queue.append(playlist_url)
        elif choice == "3":
            # Download the videos in the queue
            for video_url in queue:
                # Download the video
                print("Plese be intouch the video is being downlode in background \n don't close the window or terminate please")
                download_youtube_video(video_url)

            # Clear the queue
            queue.clear()
        elif choice == "4":
            # Exit the main loop
            break

if __name__ == "__main__":
    main()
