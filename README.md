# YouTube Downloader

This is a simple Python script that allows you to download YouTube videos and playlists.

## Requirements

* Python 3
* The pytube library

## Installation

pip install pytube


## Usage

python youtube_downloader.py

The script will start by printing a menu with the following options:

Enqueue video
Enqueue playlist
Download the listed videos
Exit
To download a video, enter the video URL in the prompt and select option 1. To download a playlist, enter the playlist URL in the prompt and select option 2. To download all of the videos in the queue, select option 3. To exit the script, select option 4.

Workings
The script works by first creating a YouTube object from the video or playlist URL. It then gets the highest resolution video stream and downloads it to the download directory.

If you want to change the default download directory, you can set the download_path variable.

Example
To download the video with the URL https://www.youtube.com/watch?v=dQw4w9WgXcQ, you would enter the following command:

python youtube_downloader.py
1
https://www.youtube.com/watch?v=dQw4w9WgXcQ
The script will then download the video to the download directory.

Credits
This script was created by Gurucharan.S.



I hope this helps!
