import datetime
disconnections = []

def get_time():
    now = datetime.time()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

#wifi connectivity
import urllib.request
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        print("True")
    except:
        disconnections.append(current_time)

