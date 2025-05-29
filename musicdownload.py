import yt_dlp

def download_mix_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': r"C:\ffmpeg\bin\ffmpeg.exe",  # Update path if needed
        'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',  # Organizes output
        'noplaylist': False,  # Allows downloading the whole playlist
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'progress_hooks': [lambda d: print(f"Done: {d['filename']}") if d['status'] == 'finished' else None],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("\n📥 Downloading Mix playlist...")
            ydl.download([playlist_url])
            print("\n✅ All songs downloaded successfully!")
    except Exception as e:
        print("❌ An error occurred:", e)

if __name__ == "__main__":
    print("🎵 YouTube Mix MP3 Downloader")
    url = input("Paste the YouTube Mix playlist URL (it includes &list=RDMM...): ").strip()
    if "list=" not in url:
        print("❌ That doesn't look like a playlist URL. Please include &list=...")
    else:
        download_mix_playlist(url)
