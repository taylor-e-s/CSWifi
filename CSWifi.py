import datetime
import time
import os
import urllib.request

disconnections = []

name = ['Claire', 'Taylor']
os.system('zenity --list --title="Disconnection Times" --column="Disconnection Times" (' '.join(name))')


def main():
    while True:
        time.sleep(20)
        if not detect():
            if ask_reconnect():
                reconnect()
                time.sleep(5)
                if not detect():
                    if ask_restart():
                        restart()
                    else:
                        time.sleep(300)
            else:
                time.sleep(300)


def add_time():
#finds the current time, adds it to the list, and displays the list
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    disconnections.append(current_time)
    os.system('zenity --info --text=disconnections')


def ask_reconnect():
    if os.system('zenity --question --text="Your internet connection has been lost. Would you like to reconnect?"'):
        os.system('zenity --info --text="You have chosen not to reconnect."')
        return False
    else:
        return True


def ask_restart():
    if os.system('zenity --question --text="Reconnection failed. Would you like to restart?"'):
        os.system('zenity --info --text="You have chosen not to restart."')
        return False
    else:
        return True


def detect(host='http://google.com'):
    #checks wifi connectivity by trying to connect to google
    try:
        urllib.request.urlopen(host)
        return True
    except:
        add_time()
        return False


def reconnect():
    #disconnects and reconnects to the wifi
    os.system('netsh interface set interface "Wi-Fi" disable')
    os.system('netsh interface set interface "Wi-Fi" enable')
    os.system('netsh wlan connect name="student"')


def restart():
    os.system("shutdown /r /t 5")


main()
