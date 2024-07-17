from pytube import YouTube

# you should be able to get information about the video => number of views, title, etcPIP
# download the video

link = input('Provide YouTube video url: ')

yt = YouTube(link)

def video_description():
    '''provides a brief description of the video you want to download'''

    try:
        # the author of  the video
        print('Author:', yt.author)

        # the title of the video
        print('Title:', yt.title)

        # number of views the video has
        print('Views:', yt.views)

        # publish date
        print('Publish date:', yt.publish_date)
    
    except Exception:
        print('invalid url or no internet connection.')
        exit()


def download_video():
    '''downloads the video of the provided url'''
    try:
        yd = yt.streams.get_highest_resolution() #returns the highest resolution of the video 
        
    except Exception:
        print('Network disconnected.\nPlease connect network and try again.')
     
    else:
        yd.download('C:/Users/paris/Videos') #downloads the video and returns it to the provided path
        print('\nVideo successfully downloaded.')


video_description()
print('\ndownloading......')    
download_video()






