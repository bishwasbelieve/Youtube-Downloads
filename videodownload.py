import sys
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'ffmpeg_location': r"C:\ffmpeg\bin\ffmpeg.exe",  # Double-check this path
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Correct spelling
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading the video in 1080p or best available...")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", e)
        input("Press Enter to exit...")  # Keeps window open to view error

if __name__ == "__main__":
    try:
        video_url = input("Enter the YouTube video URL: ").strip()
        if not video_url:
            print("No URL provided. Exiting program.")
            sys.exit(1)

        download_video(video_url)
    except Exception as e:
        print("Unexpected error:", e)
        input("Press Enter to exit...")
