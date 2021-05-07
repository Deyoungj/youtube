import PySimpleGUI as sg
import time
from time import sleep
 
#With this example... It Just auto runs from 0 to completion... this is not what I want to do, but this is teh example the creator gives
def CustomMeter():
  
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(100, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]
 
 
    window = sg.Window('Custom Progress Meter').Layout(layout)
    progress_bar = window.FindElement('progress')
   
    for i in range(100):
        
        event, values = window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        
        progress_bar.UpdateBar(i+1)
     
    window.Close()
 
CustomMeter()
 
