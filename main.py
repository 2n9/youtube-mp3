import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  '%(id)s.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

def main():
    url = input("Enter a URL: ")
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    with ydl:
        res = ydl.extract_info(url, download=True)

# call main
if __name__ == "__main__":
    main()
