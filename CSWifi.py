import datetime
import os
disconnections = []

def get_time():
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

os.system('zenity --question --text="Does this work?"')

#wifi connectivity
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        print("True")
    except:
        disconnections.append(current_time)

