import sys
import os

from pytubefix import YouTube

OUTPUT_DIRECTORY: str = "output"

def main():
    failed_urls: list[str] = []
    if len(sys.argv) <= 1:
        print("no urls given. exiting...")
        return
    os.makedirs("output", exist_ok=True)
    for url in sys.argv[1:]:
        try:
            yt: YouTube = YouTube(url)
            yt.title = yt.title.strip().replace(" ", "-")
            yt.streams.get_audio_only().download(output_path=OUTPUT_DIRECTORY, filename=f"{yt.title}.mp4")
        except:
            print(f"something went wrong with (url: ${url}). moving next.")
            failed_urls.append(url)
            continue
    if failed_urls:
        print(f"failed urls: {failed_urls}")


if __name__ == "__main__":
    main()
