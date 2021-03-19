import datetime
import time
import os
import urllib.request
import sys

disconnections = []

def main():
    while True:
        if detect() == False:
            if ask_reconnect() == True:
                reconnect()
                time.sleep(5)
                if detect() == False:
                    if ask_restart() == True:
                        restart()
                    else:
                        time.sleep(300)
            else:
                time.sleep(300)
    time.sleep(20)


def add_time():
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    disconnections.append(current_time)

def ask_reconnect():
    if os.system('zenity --question --text="Your internet connection has been lost. Would you like to reconnect?"'): #if 'No' is clicked
        os.system('zenity --info --text="You have chosen not to reconnect."')
        return False
    else: #if 'Yes' is clicked
        os.system('zenity --info --text="Reconnecting..."')
        return True

def ask_restart():
    if os.system('zenity --question --text="Reconnection failed. Would you like to restart?"'): #if 'No' is clicked
        os.system('zenity --info --text="You have chosen not to restart."')
        return False
    else: #if 'Yes' is clicked
        os.system('zenity --info --text="Restarting..."')
        return True

def detect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        add_time()
        return False

def reconnect():
    os.system('netsh interface set interface "Wi-Fi" disable')
    os.system('netsh interface set interface "Wi-Fi" enable')
    os.system('netsh wlan connect name="student"')

def restart():
    os.system("shutdown -r")

main()
