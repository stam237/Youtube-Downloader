# Projet de youtube downloader 

from pytube import YouTube

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_download = stream.filesize - bytes_remaining
    percent = (bytes_download*100)/stream.filesize
    print(f"progression du telechargement {int(percent)} %")

#recuperer l'url de la
def get_video_url_from_user():
    while True:
        url = input("donnez l'url de la video Youtube a telecharger: ")
        if "https://www.youtube.com" in url:
            print("Good url")
            return url
        print("Bad url")

def get_streaming_itag_from_user(streams_list):
    while True:
        try:
            choice = int(input("faites votre choix: "))
        except ValueError:
            print("Vous devez saisir un nombre")
            continue

        if choice in range(1,len(streams_list)+1):
            break
        else:
            print("Bad choice")
            continue
    itag = streams_list[choice-1].itag
    return itag


#cree un objet Youtube

url = get_video_url_from_user()

#create youtub video object
youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITRE: " + youtube_video.title)
print("NB Vue: ", youtube_video.views)
print("STREAM")

streams_list = youtube_video.streams.filter(progressive=True)

i = 1
for stream in streams_list:
    print(f"{i}: {stream.resolution}")
    i+=1

itag = get_streaming_itag_from_user(streams_list)

stream = youtube_video.streams.get_by_itag(itag)
print("stream_Video", stream)
print("Telechergement . . .")
stream.download()
print("OK")


#Demander le choix de la résolution


