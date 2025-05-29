import sys
import yt_dlp

def download_audio_as_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': r"C:\ffmpeg\bin\ffmpeg.exe",  # Update this if ffmpeg is elsewhere
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # You can set this to 128, 192, or 320
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio as MP3...")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ").strip()
    if not video_url:
        print("No URL provided. Exiting program.")
        sys.exit(1)

    download_audio_as_mp3(video_url)
