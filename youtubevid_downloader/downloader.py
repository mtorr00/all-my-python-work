from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    print(youtubeObject.metadata)
    print(youtubeObject.title)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)

#this should work but comp having issue resolving YouTube Object maybe something blocking access