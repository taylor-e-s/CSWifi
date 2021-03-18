import datetime
import os
import urllib.request
from urllib3.util import current_time
disconnections = []


def add_time():
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    disconnections.append(current_time)

def ask_reconnection():
    if os.system('zenity --question --text="Your internet connection has been lost. Would you like to reconnect?"'): #if 'No' is clicked
        os.system('zenity --info --text="You have chosen not to reconnect."')
    else: #if 'Yes' is clicked
        os.system('zenity --info --text="Reconnecting..."')
        return True

def ask_restart():
    if os.system('zenity --question --text="Reconnection failed. Would you like to restart?"'): #if 'No' is clicked
        os.system('zenity --info --text="You have chosen not to restart."')
    else: #if 'Yes' is clicked
        os.system('zenity --info --text="Restarting..."')
        return True

#wifi connectivity
def detect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        add_time()
        if ask_question() == True:

def reconnect():
    os.system('netsh interface set interface "Wi-Fi" disable')
    os.system('netsh interface set interface "Wi-Fi" enable')
    os.system('netsh wlan connect name="student"')

def restart():
    os.system("shutdown -r")
