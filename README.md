# YouTube Downloader

This is a simple Python script that allows you to download YouTube videos and playlists.

## Requirements

* Python 3
* The pytube library
* PySimpleGUI
* ThreadPoolExecutor
*concurrent.futures

## Installation
```
pip install pytube
pip install PySimpleGUI
pip install ThreadPoolExecutor
pip install concurrent.futures
```


## Usage

python3 main.py

The script will start by printing a menu with the following options:

Enqueue video
```
Example: 
inputing URL 
1)  https://youtu.be/dQw4w9WgXcQ
             (OR)
           USE COMMA 
2) https://youtu.be/dQw4w9WgXcQ , https://youtu.be/dQw4w9WgXcQ
```
Enqueue playlist
Download the listed videos
Exit
To download a video, enter the video URL in the prompt and select option 1. To download a playlist, enter the playlist URL in the prompt and select option 2. To download all of the videos in the queue, select option 3. To exit the script, select option 4.

Workings
The script works by first creating a YouTube object from the video or playlist URL. It then gets the highest resolution video stream and downloads it to the download directory.

If you want to change the default download directory, you can set the download_path variable.

Example
To download the video with the URL https://www.youtube.com/watch?v=dQw4w9WgXcQ, you would enter the following command:

python3 main.py


![Screenshot from 2023-07-28 16-01-53](https://github.com/GurucharanSavanth/Youtube_Downloder/assets/70633240/813118ed-445e-4659-b471-c82ac15d1f6b)

![Screenshot from 2023-07-28 16-06-26](https://github.com/GurucharanSavanth/Youtube_Downloder/assets/70633240/f97b2586-3ed0-4d07-9d98-8241fe2639ca)

https://www.youtube.com/watch?v=dQw4w9WgXcQ


The script will then download the video to the download directory.

## Credits

This script was created by Gurucharan.S.


## Updates

* The script has been optimized to download videos more efficiently.
* The code has been documented to make it easier to understand.
* The README.md file has been updated to reflect the latest changes.

## Known Issues

* The script may not work on all versions of Python.
* The script may not work on all videos.

## Donload direct executable  https://github.com/GurucharanSavanth/Youtube_Downloder/releases
