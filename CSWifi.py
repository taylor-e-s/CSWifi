import datetime
import os
import urllib.request
from urllib3.util import current_time

disconnections = []


def get_time():
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")


def ask_question():
    if os.system(
            'zenity --question --text="Your internet connection has been lost. Would you like to reconnect?"'):  # if 'No' is clicked
        os.system('zenity --info --text="You have chosen not to reconnect."')
    else:  # if 'Yes' is clicked
        os.system('zenity --info --text="That function is not ready yet."')  #


#os.system("shutdown -r -t 0")

# wifi connectivity
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        disconnections.append(current_time)
        ask_question()
