import datetime
import time
import os
import urllib.request

disconnections = []


def main():
    file1 = open("Disconnections.txt", "w")
    file1.writelines(Disconnection Times)
    file1.close()
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
    file1 = open("Disconnections.txt", "a")  # append mode
    file1.write(current_time)
    file1.close()


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
