import yt_dlp
import os
from colorama import init, Fore, Style

init()

REQUIRES = ["colorama", "yt_dlp"]


if not os.path.exists("/data/data/com.termux/files/usr/bin/ffmpeg"):
    os.system("pkg install ffmpeg -y")

download_path = "/storage/emulated/0/Download"

if not os.path.exists(download_path):
    download_path = "/sdcard/Download"

if not os.path.exists(download_path):
    download_path = os.path.expanduser("~/Downloads")

def run():

    print(Fore.CYAN + "\n== YOUTUBE DOWNLOADER ==" + Style.RESET_ALL)
    print("| 1 = MP4")
    print("| 2 = MP3")

    choice = input("| choice > ")

    
    if choice == "1":

        url = input(Fore.RED + "| YouTube URL (mp4) > " + Style.RESET_ALL)

        options = {
            "format": "bestvideo[height<=1080][vcodec=vp9]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"{download_path}/%(title)s.%(ext)s",
            "postprocessor_args": ["-threads", "2"],
            "ffmpeg_location": "/data/data/com.termux/files/usr/bin",
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print(Fore.GREEN + "| MP4 download finished" + Style.RESET_ALL)

    
    elif choice == "2":

        url = input(Fore.RED + "| YouTube URL (mp3) > " + Style.RESET_ALL)

        options = {
            "format": "bestaudio/best",
            "outtmpl": f"{download_path}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "ffmpeg_location": "/data/data/com.termux/files/usr/bin",
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print(Fore.GREEN + "| MP3 conversion finished" + Style.RESET_ALL)

    else:
        print(Fore.RED + "| invalid choice" + Style.RESET_ALL)
