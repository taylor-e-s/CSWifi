#Taylor Shirk  Claire DeVinney
from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
# detect when disconnected and add time to an array