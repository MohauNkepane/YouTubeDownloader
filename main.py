import requests
from pytube import YouTube


def urltitle(url):
    yt = YouTube(url)
    print(yt.title)
    getthumbnail(yt.thumbnail_url)





def getthumbnail(url):
    r = requests.get(url)
    if r.status_code == 200:
        # Extracting Picture from response
        file = open("thumb.png", "wb")
        file.write(r.content)
        file.close()
    else:
        print("Could not get Thumbnail")


def downloadVideo(url="https://www.youtube.com/watch?v=l3zhOoDKVvs"):
    yt = YouTube(url)
    # Legacy Streams | With both Video and Audio | 720p and below
    yt.streams.filter(progressive=True).get_by_resolution("720p").download()
    # print(yt.streams.filter(progressive=True))
    print(f"Downloaded {yt.title}")


if __name__ == '__main__':
    # urltitle(input("Paste Youtube Url Here: "))
    # print_hi('PyCharm')
    downloadVideo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
