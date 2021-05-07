from pytube import YouTube
import PySimpleGUI as sg





a ='https://www.youtube.com/watch?v=vwAdfv8ZXLM4'

def download(url):
           
    yt = YouTube(url)
      


def title(url):
    try:
        yt = YouTube(url)
        return yt.title
    except:
        # window['-FEED-BACK-'].pdar
        pass

def lenth(url):
    
    try:
        yt = YouTube(url)
        return yt.length
    except:
        window['-FEED-BACK-'].update('connectiontime out')
        pass
    
def rating(url):
    
    try:
        yt = YouTube(url)
        return yt.rating
    except:
        window['-FEED-BACK-'].update('connectiontime out')
        pass
# def size(url):
    # yt = YouTube(url)
    
#     return str(round(yt.filesize/(1024*1024)))

def views(url):
    try:
        yt = YouTube(url)
        return yt.views
    except:
        window['-FEED-BACK-'].update('connection time out')
        pass


def feed_back(res, word):
    window[res].update(f'Please enter a {word} url',text_color='red')
    


def progress():
    pass
    
    
    
   
    

def download_mp4(url,path):
    
    yt = YouTube(url)
    
    try:
        window['_DPROG_'].update('Downloading video')
        
        yt.streams.first().download(path)
        
        window['_DPROG_'].update('Download complete')
    except:
        window['_DPROG_'].update('connctiontime out', text_color='red')
        
        
        
        
        
        
def download_mp3(url,path):
    
    yt = YouTube(url)
    
    try:
        window['_DPROG_'].update('Downloading Audio')
        
        yt.streams.filter(only_audio=True).first().download(path)
        
        window['_DPROG_'].update('Download complete')
    except:
        window['_DPROG_'].update('connctiontime out',text_color='red')
    
    





sg.theme('DarkGrey14')



layout = [
    
    [sg.Text('video Downloader', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE, pad=(0,20))],
    
    [sg.Text('Video url',pad=(21,12)),sg.Input(key='-URL-',),sg.Button('Search')],
    
    [sg.Text(size=(40,1), key='-FEED-BACK-')],
    
    [sg.Text('download path',pad=(4,12)),sg.Input('/home/chidi/Downloads',key='input'),sg.FolderBrowse('Browse',initial_folder='/home/chidi/Downloads')],
    
    [sg.Radio('MP4','-MP-',key='-MP4-')],
    
    [sg.Radio('MP3','-MP-', key='-MP3-')],
    
    [sg.Text(pad=(5,3),)],
    
    
    [sg.Text('Title: ',text_color='green'),sg.Text(size=(40,1), key='-TITLE-')],
    
    
    [sg.Text('Rating:: ',text_color='green'),sg.Text(size=(40,1), key='-RATING-')],
    
    [sg.Text('Size: ',text_color='green'),sg.Text(size=(40,1), key='-SIZE-')],
    
    [sg.Text('lenth: ',text_color='green'),sg.Text(size=(40,1), key='-LENTH-')],
    
    [sg.Text('views: ',text_color='green'),sg.Text(size=(40,1), key='-VIEWS-')],
    
    [sg.Text(pad=(5,3),)],
    
    [sg.Text(size=(40,1), key='_DPROG_',text_color='green')],
    
    [sg.ProgressBar(100, orientation='h', size=(25,20), key='-PROG-',),sg.Text('0'+ ' %',key = '-PRO-')],
    
    [sg.Button('Download',pad=(0,4),button_color=('white','springgreen4'))]
]







window = sg.Window('Download_vid',layout=layout, icon = 'ytdl.ico',)
Progressbar = window['-PROG-']



while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Search':
        
        url = values['-URL-']
        
        if url == '':
            feed_back('-FEED-BACK-','video')
            
        if url != '':
            
            try:
                window['-TITLE-'].update(title(url))
                
                
                window['-RATING-'].update(rating(url))
                
                # window['-SIZE-'].update(size(url) + ' MB')
                
                window['-LENTH-'].update(lenth(url))
                
                window['-VIEWS-'].update(views(url))
            except:
                window['-FEED-BACK-'].update('connection timeout!')
          
    
    
        
    if event == 'Download':
        
        
       
        
        if values['-URL-'] == '':
            feed_back('-FEED-BACK-','video')
            
            
        elif values['-MP4-'] == True:
            print('downloading')
            # window['_DPROG_'].update('Downloading video')
            download_mp4(values['-URL-'],values['input'])
            # window['_DPROG_'].update('Download complete')
            
        
        elif values['-MP3-'] == True:
            print('downloading')
            # window['_DPROG_'].update('Downloading video')
            download_mp3(values['-URL-'], values['input'])
            # window['_DPROG_'].update('Download complete')
            
        
                
        
                
                
            
        
        
        
        
